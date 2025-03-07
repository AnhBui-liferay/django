from django.shortcuts import render, redirect
import requests
from api.documents import BlogPostDocument
from api.models import BlogPost

API_URL = "http://127.0.0.1:8000/api/blogs/"  # Update if needed

def blog_list(request):
    response = requests.get(API_URL)
    blogs = response.json() if response.status_code == 200 else []
    return render(request, "frontend/blog_list.html", {"blogs": blogs})

def create_blog(request):
    if request.method == "POST":
        data = {
            "title": request.POST["title"],
            "content": request.POST["content"]
        }
        response = requests.post(API_URL + "new/", json=data)
        if response.status_code == 201:
            return redirect("blog_list")

    return render(request, "frontend/create_blog.html")

def delete_blog(request, post_id):
    if request.method == "POST":
        response = requests.delete(f"{API_URL}{post_id}/delete/")
        if response.status_code == 204:
            return redirect("blog_list")
    
    return redirect("blog_list")

def search_blog(request):
    """ Search for blog posts using Elasticsearch """
    query = request.GET.get('query', '')

    if query:
        search_results = BlogPostDocument.search().query("multi_match", query=query, fields=["title", "content"])[:10]
        blog_ids = [result.meta.id for result in search_results]  # Extract the IDs
        blogs = BlogPost.objects.filter(id__in=blog_ids)  # Fetch real ORM objects
    else:
        blogs = BlogPost.objects.all()

    return render(request, 'frontend/blog_list.html', {'blogs': blogs})

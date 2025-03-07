from django.urls import path
from .views import blog_list, create_blog, delete_blog, search_blog

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('new/', create_blog, name='create_blog'),
    path('<int:post_id>/delete/', delete_blog, name='delete_blog'),
    path('search/', search_blog, name='search_blog'),
]

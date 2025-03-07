from django.urls import path
from .views import get_blog_posts, create_blog_post, delete_blog_post

urlpatterns = [
    path('blogs/', get_blog_posts, name='get_blog_posts'),
    path('blogs/new/', create_blog_post, name='create_blog_post'),
    path('blogs/<int:post_id>/delete/', delete_blog_post, name='delete_blog_post'),
]

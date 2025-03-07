from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import BlogPost
from .serializer import BlogPostSerializer

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_blog_posts(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    serializer = BlogPostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def create_blog_post(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def delete_blog_post(request, post_id):
    try:
        post = BlogPost.objects.get(id=post_id)
        post.delete()
        return Response({"message": "Blog post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except BlogPost.DoesNotExist:
        return Response({"error": "Blog post not found"}, status=status.HTTP_404_NOT_FOUND)

from django.db import models
from django.core.files.storage import default_storage

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(storage=default_storage, upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
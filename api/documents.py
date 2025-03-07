from django_elasticsearch_dsl.documents import Document
from django_elasticsearch_dsl.registries import registry
from .models import BlogPost

@registry.register_document
class BlogPostDocument(Document):
    class Index:
        name = 'blog_posts'
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = BlogPost
        fields = ['title', 'content']

    class Meta:
        timeout = 60  # Increase timeout
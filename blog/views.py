from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost, Blog
from .serializers import BlogPostSerializer, BlogSerializer

# API view to list all blog posts
class BlogPostList(ListAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer

# API view to retrieve a single blog post by ID
class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'  # Ensure it matches the URL conf

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='blog_images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=255, blank=True)
    share_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
# models.py
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.urls import path
from .views import BlogPostList

urlpatterns = [
    path('api/', BlogPostList.as_view(), name='blog-api'),
]

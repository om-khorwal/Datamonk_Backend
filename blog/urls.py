from django.urls import path
from .views import BlogPostList, BlogDetailView

urlpatterns = [
    path('api/', BlogPostList.as_view(), name='blog-list'),
    path('api/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
]

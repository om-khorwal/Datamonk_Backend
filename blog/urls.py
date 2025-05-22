# from django.urls import path
# from .views import BlogPostList, BlogDetailView

# urlpatterns = [
#     path('api/', BlogPostList.as_view(), name='blog-api'),
#     path('api/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
# ]
    
from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.BlogList.as_view(), name='blog-api'),
    path('api/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
]

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=False, allow_null=False)

    class Meta:
        model = BlogPost
        fields = '__all__'
    
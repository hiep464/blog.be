from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image']

class BlogHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'short_description', 'image']

class BlogLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['link']

class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'link', 'category', 'content', 'created_at']
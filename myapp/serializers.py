from .models import Blog, LinkYoutube, UserRegister
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image']

class BlogHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'short_description', 'image', 'created_at']

class BlogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'category', 'content', 'created_at']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkYoutube
        fields = ['id', 'title', 'link', 'short_description']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ['name', 'phone', 'email']

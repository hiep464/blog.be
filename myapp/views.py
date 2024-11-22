from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import BlogSerializer, UserRegisterSerializer, WebInfoSerializer, PageSerializer
from .models import Blog, UserRegister, WebInfo, Page
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


from django_filters import rest_framework as filters

class BookFilter(filters.FilterSet):
    category_title = filters.CharFilter(field_name='category__title', lookup_expr='icontains')  # Lọc không phân biệt hoa/thường

    class Meta:
        model = Blog
        fields = ['category']

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    filterset_fields = ['category__name', 'sub_category']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['^sub_category__name']

class UserRegisterViewSet(ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = UserRegisterSerializer
    filter_backends = [DjangoFilterBackend]

class WebInfoViewSet(ModelViewSet):
    queryset = WebInfo.objects.all()
    serializer_class = WebInfoSerializer
    filter_backends = [DjangoFilterBackend]

class PageViewSet(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']

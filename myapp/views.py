from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import BlogSerializer, BlogDetailSerializer, BlogHomeSerializer, BlogLinkSerializer
from .models import Blog
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django.db.models import Q


class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BlogAPIView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    pagination_class = BlogPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']  # Thêm các trường bạn muốn tìm kiếm


class BlogViews(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, category, page_idx):
        try:
            blogs = Blog.objects.filter(category=category).order_by("created_at")
            items_per_page = 10
            paginator = Paginator(blogs, items_per_page)
            data = paginator.page(page_idx)
            serializer = BlogSerializer(data, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogDetailViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, id):
        try:
            blog = Blog.objects.get(id=id)
            serializer = BlogDetailSerializer(blog)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class BlogHomeViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, category, count):
        try:
            blog = Blog.objects.filter(category=category).order_by('-created_at')[:count]
            serializer = BlogHomeSerializer(blog, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogLinkViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            blog = Blog.objects.exclude(link__isnull=True).order_by('-created_at')[:3]
            serializer = BlogLinkSerializer(blog, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogLastestViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            blog = Blog.objects.all().order_by('-created_at')[:3]
            serializer = BlogSerializer(blog, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

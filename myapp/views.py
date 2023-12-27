from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import BlogSerializer, BlogDetailSerializer, BlogHomeSerializer, LinkSerializer, UserRegisterSerializer
from .models import Blog, LinkYoutube, UserRegister
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
    serializer_class = BlogHomeSerializer
    queryset = Blog.objects.all()
    pagination_class = BlogPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content', 'short_description']  # Thêm các trường bạn muốn tìm kiếm


class BlogViews(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, category, page_idx):
        try:
            blogs = Blog.objects.filter(category=category).order_by("created_at")
            items_per_page = 10
            paginator = Paginator(blogs, items_per_page)
            data = paginator.page(page_idx)
            serializer = BlogHomeSerializer(data, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogPageViews(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, category):
        try:
            blogs = Blog.objects.filter(category=category).order_by("created_at")
            items_per_page = 10
            paginator = Paginator(blogs, items_per_page)
            response_data = {
                'num_pages': paginator.num_pages
            }
            return JsonResponse(
                data=response_data, status=status.HTTP_200_OK, safe=False
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

class LinkViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, category, count):
        try:
            links = LinkYoutube.objects.filter(type_video=category).order_by('-created_at')[:count]
            serializer = LinkSerializer(links, many=True)
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
            blog = Blog.objects.all().order_by('-created_at')[:6]
            serializer = BlogSerializer(blog, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogFeatureViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            blog = Blog.objects.filter(featured=True).order_by('-created_at')[:6]
            serializer = BlogSerializer(blog, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class BlogInfoViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            blog = Blog.objects.filter(category="INFO").order_by('-created_at')[:1]
            serializer = BlogDetailSerializer(blog, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserRegisterViews(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

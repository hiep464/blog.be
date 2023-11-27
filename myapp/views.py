from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import status


class BlogViews(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            blogs = Blog.objects.all().order_by("created_at")
            serializer = BlogSerializer(blogs, many=True)
            return JsonResponse(
                data=serializer.data, status=status.HTTP_200_OK, safe=False
            )
        except Exception as e:
            return JsonResponse(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


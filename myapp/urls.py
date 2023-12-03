from django.urls import include, path
from .views import BlogViews

urlpatterns = [
    path("api/blog", BlogViews.as_view(), name="get all blog"),
]
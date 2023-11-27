from django.urls import include, path
from .views import BlogViews

urlpatterns = [
    path("blog", BlogViews.as_view(), name="get all blog"),
]
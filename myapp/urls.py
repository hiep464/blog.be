from django.urls import include, path
from .views import BlogViews, BlogDetailViews, BlogAPIView, BlogHomeViews, BlogLinkViews, BlogLastestViews

urlpatterns = [
    path("api/blog", BlogViews.as_view(), name="get all blog"),
    path("api/blog/<int:id>", BlogDetailViews.as_view(), name="get all blog"),
    path("api/blog/<str:category>/<int:page_idx>", BlogViews.as_view(), name="get all blog"),
    path('api/search', BlogAPIView.as_view(), name='search'),
    # path('api/home', BlogHomeViews.as_view(), name='search'),
    path('api/home/<str:category>/<int:count>', BlogHomeViews.as_view(), name='filter by category'),
    path('api/link', BlogLinkViews.as_view(), name='link'),
    path('api/blog/lastest', BlogLastestViews.as_view(), name='blog lastest'),
]
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, UserRegisterViewSet, WebInfoViewSet, PageViewSet
from django.conf.urls.i18n import i18n_patterns


router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'user-registers', UserRegisterViewSet)
router.register(r'web-info', WebInfoViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # Đường dẫn cho set_language
]
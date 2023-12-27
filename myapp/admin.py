from django.contrib import admin
from .models import Blog, LinkYoutube, UserRegister
from rangefilter.filters import (
    DateRangeFilterBuilder,
)

class BlogAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextField()},
    # }
    search_fields = [
        'title',
    ]
    list_display = ('id', 'title')
    list_filter = ["category", "featured"]

admin.site.register(Blog, BlogAdmin)

class LinkYoutubeAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
    ]
    list_display = ('id', 'title')
    list_filter = ["type_video"]

admin.site.register(LinkYoutube, LinkYoutubeAdmin)

class UserRegisterAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'phone',
        'email',
    ]
    list_display = ('name', 'phone', 'email', 'created_at')
    list_filter = [("created_at", DateRangeFilterBuilder(title="Ngày đăng ký"))]

admin.site.register(UserRegister, UserRegisterAdmin)

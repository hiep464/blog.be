from django.contrib import admin
from .models import Blog, UserRegister, SubCategory, WebInfoLink, WebInfoHotline, Category, WebInfo, Page
from rangefilter.filters import (
    DateRangeFilterBuilder,
)

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    fields = ['name']
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [SubCategoryInline]

admin.site.register(Category, CategoryAdmin)

class WebInfoLinkInline(admin.TabularInline):
    model = WebInfoLink
    fields = ('type', 'url')
    extra = 5

class WebInfoHotlineInline(admin.TabularInline):
    model = WebInfoHotline
    fields = ('type', 'phone')
    extra = 5

class WebInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [WebInfoLinkInline, WebInfoHotlineInline]

admin.site.register(WebInfo, WebInfoAdmin)

class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')

admin.site.register(Page, PageAdmin)

class BlogAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
    ]
    list_display = ('id', 'title', 'category', "sub_category")

    list_filter = ['category', "sub_category"]

    def category(self, obj):
        return obj.category.name
    

admin.site.register(Blog, BlogAdmin)

class UserRegisterAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
        'phone',
        'email',
    ]
    list_display = ('name', 'phone', 'email', 'created_at')
    list_filter = [("created_at", DateRangeFilterBuilder(title="Ngày đăng ký"))]

admin.site.register(UserRegister, UserRegisterAdmin)

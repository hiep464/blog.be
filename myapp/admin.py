from django.contrib import admin
from .models import Blog, LinkYoutube, UserRegister

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
    list_display = ('email', 'phone', 'email')

admin.site.register(UserRegister, UserRegisterAdmin)

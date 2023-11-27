from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextField()},
    # }
    search_fields = [
        'title',
    ]
    list_display = ('id', 'title')

admin.site.register(Blog, BlogAdmin)

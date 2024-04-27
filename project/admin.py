from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username',)

admin.site.register(Post, PostAdmin)

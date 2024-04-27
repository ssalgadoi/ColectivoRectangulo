from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('-published',)
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'published')

admin.site.register(Post, PostAdmin)

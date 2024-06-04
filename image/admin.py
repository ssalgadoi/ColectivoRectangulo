from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1  # Número de formularios vacíos a mostrar

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published')
    ordering = ('-published',)
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'published')
    inlines = [PostImageInline]

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)
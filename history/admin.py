

from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_category')  # Cambiado 'post_categories' a 'post_category'
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'category__name')

    def post_category(self, obj):
        return ", ".join([c.name for c in obj.category.all().order_by("name")])  # Cambiado 'categories' a 'category'
    post_category.short_description = "Categorías"  # Cambiado 'post_categories' a 'post_category'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

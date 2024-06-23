from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def history(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "history/historias.html", {'posts': posts, 'categories': categories})

def historia(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "history/historia.html", {'post': post})

def category(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    posts = category.get_posts.all()
    return render(request, "history/category.html", {'category': category, 'categories': categories, 'posts': posts})

def audiovisual(request):
    category = get_object_or_404(Category, name="Más")
    posts = Post.objects.filter(category=category)
    return render(request, "history/videos.html", {'posts': posts})

def video_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "history/video.html", {'post': post})

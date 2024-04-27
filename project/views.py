from django.shortcuts import render, get_object_or_404
from .models import Post
from history.models import Category 

# Create your views here.

def project(request):
    posts = Post.objects.all()
    return render(request, "project/proyectos.html", {'posts': posts})

# def portafolio(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, "project/portafolio.html", {'post': post})

# def project_category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     return render(request, "project/category.html", {'category': category})

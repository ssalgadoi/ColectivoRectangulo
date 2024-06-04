from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

def about(request):
    posts = Post.objects.all()
    return render(request, "about/nosotros.html", {'posts': posts})

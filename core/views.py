from django.shortcuts import render
from history.models import Post

# Create your views here.

def core(request):
    return render(request, "core/base.html")

def home(request):
    posts = Post.objects.all()
    return render(request, "core/home.html", {'posts': posts})



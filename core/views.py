from django.shortcuts import render
from history.models import Post as HistoryPost
from image.models import Post 

# Create your views here.

def core(request):
    return render(request, "core/base.html")

def home(request):
    history_posts = HistoryPost.objects.all()
    posts = Post.objects.all()
    context = {
        'history_posts': history_posts,
        'posts': posts,
    }
    return render(request, "core/home.html", context)
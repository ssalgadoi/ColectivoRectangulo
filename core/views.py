from django.shortcuts import render
from history.models import Post as HistoryPost


# Create your views here.

def core(request):
    return render(request, "core/base.html")

def home(request):
    history_posts = HistoryPost.objects.all()
    posts = HistoryPost.objects.all()
    context = {
        'history_posts': history_posts,
        'posts': posts,
    }
    return render(request, "core/home.html", context)
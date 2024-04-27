from django.shortcuts import render, get_object_or_404
from .models import Post
# from history.models import Category

# Create your views here.

def audiovisual(request):
    posts = Post.objects.all()
    return render(request, "audiovisual/videos.html", {'posts':posts})

def video(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "audiovisual/video.html", {'post': post})


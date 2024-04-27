from django.urls import path
from . import views

urlpatterns = [
    path('', views.audiovisual, name="videos"),
    path('video/<int:post_id>/', views.video, name="video"),
    # path('category/<int:category_id>/', views.video_category, name="video_category"),
]
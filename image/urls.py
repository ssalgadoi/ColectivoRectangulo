from django.urls import path
from . import views

urlpatterns = [
    path('', views.image, name="fotografias"),
    path('fotografia/<int:post_id>/', views.fotografia, name="fotografia"),
    path('category/<int:category_id>/', views.image_category, name="image_category"),
]
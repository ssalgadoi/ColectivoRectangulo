from django.urls import path
from . import views

urlpatterns = [
    path('', views.project, name="proyectos"),
    path('proyecto/<int:post_id>/', views.project, name='proyecto'),
    # path('portafolio/', views.portafolio, name="portafolio"),
    # path('category/<int:category_id>/', views.project_category, name="category"),
]
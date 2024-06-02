from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción", null=True, blank=True)
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog")
    video = EmbedVideoField(verbose_name="Enlace del video", help_text="Ingrese el enlace del video de Vimeo")
    data = models.CharField(max_length=200, verbose_name="Datos")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") 
    
    class Meta:
        verbose_name = "historia"
        verbose_name_plural = "historias"
        ordering = ['-created']

    def __str__(self):
        return self.title
    

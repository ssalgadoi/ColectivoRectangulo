from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# from history.models import Category  
from embed_video.fields import EmbedVideoField

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.CharField(max_length=200, verbose_name="Descripción", null=True, blank=True)
    content = models.TextField(verbose_name="Contenido", null=True, blank=True)
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    # video = EmbedVideoField(verbose_name="Enlace del video", null=True, blank=True, help_text="Ingrese el enlace del video de Vimeo")
    # data = models.CharField(max_length=200, verbose_name="Datos", null=True, blank=True)
    url = models.URLField(verbose_name="Url del proyecto", max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name="proyect_posts")
    # category = models.ManyToManyField(Category, verbose_name="Categoría", related_name="proyect_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['-created']

    def __str__(self):
        return self.title


    
    # Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Nombre")
#     created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
#     updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

#     class Meta:
#         verbose_name = "categoría"
#         verbose_name_plural = "categorías"
#         ordering = ['-created']

#     def __str__(self):
#         return self.name
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# from history.models import Category 

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name="image_posts")
    # category = models.ManyToManyField(Category, verbose_name="Categoría", related_name="image_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes"
        ordering = ['-created']

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagenes')
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)

    class Meta:
        verbose_name = "Imagen de post"
        verbose_name_plural = "Imágenes de post"
        
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
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name="Ingresa tu nombre")
    email = models.EmailField(max_length=20,verbose_name="Escribe tu email")
    message = models.TextField(max_length=100,verbose_name="Escribe tu mensaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        ordering = ['-created']

    def __str__(self):
        return self.name
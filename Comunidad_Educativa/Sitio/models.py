from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Publicacion(models.Model):
    tipoPublicacion = (
        ('Primario', 'Primario'),
        ('Secundario','Secundario'),
        ('Universitarios','Universitarios'),         
    )

    estadoPublicacion = (
        ('Publicado','Publicado'),
        ('Borrador','Borrador'),
        ('Denunciado','Denunciado'),
        ('Eliminado','Eliminado'),
    )
    idPublicacion = models.AutoField(primary_key= True)
    idUsuarioPublicacion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tituloPublicacion = models.CharField(blank=False, max_length = 50)
    tipoPublicacion = models.CharField(choices=tipoPublicacion, null=True, blank=True,max_length = 50)
    estadoPublicacion = models.CharField(choices=estadoPublicacion, null=True, blank=True,max_length = 50)
    Contenido = models.TextField(blank=False)
    precio = models.TextField(blank=False)
    FechaPublicacion = models.DateField(("Date"), auto_now=True, editable = False)
    FechaBajaPublicacion = models.DateField(default= None, editable = False,null = True)
    FechaModificacionPublicacion = models.DateField(default = None, editable = False, null = True)

    def __str__(self):
        return (self.tituloPublicacion)


    def get_absolute_url(self):
        return reverse ('nuevapublicacion', args=[str(self.idPublicacion)])

class Comment(models.Model):
    post = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
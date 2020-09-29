from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.


class Publicacion(models.Model):
    tipoPublicacion = (
        ('Primario', 'Nivel Primario'),
        ('Secundario','Nivel Secundario'),
        ('Universitarios','Nivel Universitarios'),
    )

    estadoPublicacion = (
        ('Publicado','Publicado'),
        ('Borrador','Borrador')
    )
    Materias = (
        ('Matemáticas','Matemáticas'),
        ('Sociales','Ciencias Sociales'),
        ('Naturales','Ciencias Naturales'),
        ('Lengua','Lengua'),
        ('InglesI','InglésI'),
        ('InglesII','InglésII'),
        ('InglesIII','InglésIII'),
        ('Literatura','Literatura'),
        ('Historia','Historia'),
        ('Química','Química'),
        ('Informática','Informática'),
    )

    idPublicacion = models.AutoField(primary_key= True)
    idUsuarioPublicacion = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tituloPublicacion = models.CharField(blank=False, max_length = 50)
    tipoPublicacion = models.CharField(choices=tipoPublicacion, null=True, blank=True,max_length = 50)
    estadoPublicacion = models.CharField(choices=estadoPublicacion, null=True, blank=True,max_length = 50)
    materia = models.CharField(choices=Materias,max_length=50, null=True, blank=False)
    Contenido = models.TextField(blank=False)
    precio = models.TextField(blank=False)
    FechaPublicacion = models.DateField(("Date"), auto_now=True, editable = False)
    FechaBajaPublicacion = models.DateField(default= None, editable = False,null = True)
    FechaModificacionPublicacion = models.DateField(default = None, editable = False, null = True)

    def __str__(self):
        return (self.tituloPublicacion)


    def get_absolute_url(self):
        return reverse ('nuevapublicacion', args=[str(self.idPublicacion)])

class SolicitudContacto(models.Model):
    idUsuarioSolicitante = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_create', on_delete=models.CASCADE)
    idUsuarioReceptor  =models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_receive', on_delete=models.CASCADE)

    def __str__(self):
        return (self.idUsuarioSolicitante)

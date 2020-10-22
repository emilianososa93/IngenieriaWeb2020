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
        ('Borrador','Borrador'),
        ('Oculta','Oculta'),
        ('Eliminado','Eliminado'),
        ('Denunciado','Denunciado')
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
    ubicacionGeografica =  models.TextField( null=True, blank=True,max_length = 50)
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
    estadosCargados = (
        ('Pendiente', 'Pendiente'),
        ('Rechazado', 'Rechazado'),
        ('Aceptado', 'Aceptado'),
    )

    idUsuarioSolicitante = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_create', on_delete=models.CASCADE)
    idUsuarioReceptor  =models.ForeignKey(settings.AUTH_USER_MODEL, related_name='request_receive', on_delete=models.CASCADE)
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    estadoSolicitud = models.CharField(max_length=50, choices=estadosCargados, null=True, blank=True)

    def __str__(self):
        return (self.idPublicacion.idPublicacion)

    def get_absolute_url(self):
        return reverse ('solicitarcontacto', args=[str(self.id)])


class Comentario(models.Model):
    estadosCargados = (
        ('Publicado', 'Publicado'),
        ('Denunciado', 'Denunciado'),
        ('Eliminado', 'Eliminado'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    idpublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=1000,null=True,blank=False)
    estadoComentario = models.CharField(max_length=20, choices=estadosCargados, blank=True, default='Borrador')

    def __str__(self):
        return str(self.comentario)



class Denuncia(models.Model):
    estadosCargados = (
        ('Denunciado', 'Denunciado'),
        ('Eliminado', 'Eliminado'),
    )
    
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    motivo = models.TextField()
    estadoDenuncia = models.CharField(choices=estadosCargados, null=True, blank=True,max_length = 50)

    class Meta:
        unique_together = ('idPublicacion', 'idUsuario')

    def __str__(self):
        return self.motivo
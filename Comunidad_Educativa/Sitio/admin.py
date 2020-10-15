from django.contrib import admin
from .models import Denuncia,Publicacion,SolicitudContacto,Comentario


admin.site.register(Publicacion)
admin.site.register(Denuncia)
admin.site.register(Comentario)
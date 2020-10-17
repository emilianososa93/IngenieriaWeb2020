from django.contrib import admin
from .models import Denuncia,Publicacion,SolicitudContacto,Comentario
from Login.models import Perfil


admin.site.register(Publicacion)
admin.site.register(Denuncia)
admin.site.register(Comentario)
admin.site.register(Perfil)
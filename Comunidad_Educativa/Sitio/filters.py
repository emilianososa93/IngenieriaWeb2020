import django_filters
from .models import *
from django import forms


class PublicacionFilter(django_filters.FilterSet):
    class Meta:
        model=Publicacion
        fields=['tipoPublicacion','materia','ubicacionGeografica']


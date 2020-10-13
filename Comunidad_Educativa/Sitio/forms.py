from django import forms
from django.contrib.auth.models import User
from . models import *
from django.db import models
from django.forms import ModelForm, Textarea


tipoPubli = (
        ('Primario', 'Nivel Primario'),
        ('Secundario','Nivel Secundario'),
        ('Universitarios','Nivel Universitario'),
    )
estadoPubli = (
        ('Publicado','Publicado'),
        ('Borrador','Borrador')
    )
Materias = (
        ('Matemáticas','Matemáticas'),
        ('Sociales','Sociales'),
        ('Naturales','Naturales'),
        ('Lengua','Lengua'),
        ('InglesI','InglesI'),
        ('InglesII','InglesII'),
        ('InglesIII','InglesIII'),
        ('Literatura','Literatura'),
        ('Historia','Historia'),
        ('Química','Química'),
        ('Informática','Informática'),
    )

class PublicacionForm(forms.Form):
    tipoPublicacion = forms.CharField(max_length=50, widget=forms.Select(choices=tipoPubli, attrs={'class' : 'validate form-control '}))
    estadoPublicacion = forms.CharField(max_length=50, widget=forms.Select(choices=estadoPubli, attrs={'class' : 'validate form-control '}))
    tituloPublicacion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
    precio = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
    Contenido = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={"rows":10, "cols":20,'class' : 'validate form-control'}))
    localidad = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
    provincia = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'validate form-control'}))
    imagen = forms.ImageField()
    materia = forms.CharField(max_length=50,widget=forms.Select(choices=Materias, attrs={'class' : 'validate form-control '}))

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['motivo']
        widgets = {
            'motivo': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese motivo', 'rows': '4', 'cols': '50'}),
        }

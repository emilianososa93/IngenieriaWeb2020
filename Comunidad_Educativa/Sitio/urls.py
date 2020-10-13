from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.portada, name='portada'),
    url('portada/', views.portada, name='portada_index'),
    path('nuevapublicacion/', views.nuevapublicacion, name='nuevapublicacion'),
    url('mispublicaciones/', views.mispublicaciones, name='mispublicaciones'),
    url(r'^verpublicacion/(?P<pk>[0-9]+)/$', views.verpublicacion, name='verpublicacion'),
    url(r'^editarpublicacion/(?P<pk>[0-9]+)/$', views.editarpublicacion, name='editarpublicacion'),
	url(r'^solicitarcontacto/(?P<pk>[0-9]+)/$', views.solicitarcontacto, name='solicitarcontacto'),
	url(r'^eliminarpublicacion/(?P<pk>[0-9]+)/$', views.eliminarpublicacion, name='eliminarpublicacion'),
	url(r'^nuevadenuncia/(?P<pk>[0-9]+)/$', views.nuevadenuncia, name='nuevadenuncia')
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from haystack.views import SearchView, search_view_factory
from haystack.forms import HighlightedSearchForm
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.portada, name='portada'),
    url('portada/', views.portada, name='portada_index'),
    path('nuevapublicacion/', views.nuevapublicacion, name='nuevapublicacion'),
    url('mispublicaciones/', views.mispublicaciones, name='mispublicaciones'),
    url(r'^verpublicacion/(?P<pk>[0-9]+)/$', views.verpublicacion, name='verpublicacion'),
    url(r'^editarpublicacion/(?P<pk>[0-9]+)/$', views.editarpublicacion, name='editarpublicacion'),
	url(r'^solicitarcontacto/(?P<pk>[0-9]+)/$', views.solicitarcontacto, name='solicitarcontacto'),
	url(r'^eliminarpublicacion/(?P<pk>[0-9]+)/$', views.eliminarpublicacion, name='eliminarpublicacion'),
	url(r'^search/$', search_view_factory(view_class=SearchView, form_class=HighlightedSearchForm), name='search'),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^comentariopublicacion/$', views.comentariopublicacion, name ='comentariopublicacion'),
    url(r'^verpublicacion/(?P<pk>[0-9]+)/versolicitudes/$', views.versolicitudes, name ='versolicitudes'),
    url(r'^eliminarsolicitud/(?P<pk>[0-9]+)/$', views.eliminarsolicitud, name='eliminarsolicitud'),
    url(r'^aceptarsolicitud/(?P<pk>[0-9]+)/$', views.aceptarsolicitud, name='aceptarsolicitud'),
    url(r'^nuevadenuncia/(?P<pk>[0-9]+)/$', views.nuevadenuncia, name='nuevadenuncia'),
    url(r'^activarpublicacion/(?P<pk>[0-9]+)/$', views.activarpublicacion, name='activarpublicacion'),
    url(r'^versolicitudestotales/(?P<pk>[0-9]+)/$', views.versolicitudestotales, name='versolicitudestotales'),
    
]

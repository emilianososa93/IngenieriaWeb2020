from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    url('login/',  LoginView.as_view()),
    url('logout/', views.logout),
    url(r'^bienvenido/(?P<activacion_token>\w+)/',views.confirmar),
    url(r'^confirmar/(?P<activacion_token>\w+)/', views.confirmar),
    url('validacionmail/', views.validacionmail),
    url('registrar/', views.registrar, name = 'registrar'),
    url('nosotros/', views.nosotros, name = 'nosotros'),
    url('editarusuario/', views.editarusuario, name = 'editarusuario'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .filters import PublicacionFilter
from .forms import PublicacionForm
from .models import Publicacion
from Login.models import Perfil
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect


@login_required
def nuevapublicacion(request):

	model = Publicacion
	if request.method == 'POST':
		form = PublicacionForm(request.POST)
		tipoPublicacion = request.POST['tipoPublicacion']
		materia = request.POST['materia']
		tituloPublicacion = request.POST['tituloPublicacion']
		estadoPublicacion = request.POST['estadoPublicacion']
		precio = request.POST['precio']
		Contenido = request.POST['Contenido']
		idUsuarioPublicacion = request.user
		publicacion = Publicacion(
			tipoPublicacion = tipoPublicacion,
			materia = materia,
			tituloPublicacion = tituloPublicacion,			
			estadoPublicacion = estadoPublicacion,
			precio = precio,
			Contenido = Contenido,
			idUsuarioPublicacion = idUsuarioPublicacion			
        )
		publicacion.save()


		_usuario = request.user.id
		mispublicaciones = Publicacion.objects.all().filter(idUsuarioPublicacion = _usuario)
		return render(request, 'mispublicaciones.html', {'mispublicaciones': mispublicaciones})
	else:
		form = PublicacionForm(request.POST)

	usuario  = []
	_usuario = request.user.id
	perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
	for _perfil in perfilesUsuario:
		usuario.append(Perfil.objects.all().last())

	return render(request, 'nuevapublicacion.html',{ 'form': form ,'usuario': usuario})



def mispublicaciones(request):
	_usuario = request.user.id
	mispublicaciones = Publicacion.objects.all().filter(idUsuarioPublicacion = _usuario)
	return render(request, 'mispublicaciones.html', {'mispublicaciones': mispublicaciones})


def verpublicacion(request,pk):
	form = PublicacionForm(request.POST)
	_idPublicacion = pk
	publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion).first()

	if request.method == 'POST':
		return HttpResponseRedirect('/verpublicacion/%s' %pk )

	else:
		usuario  = []
		_usuario = publicacion.idUsuarioPublicacion
		perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
		for _perfil in perfilesUsuario:
			usuario.append(Perfil.objects.all().last())


	return render(request, 'verpublicacion.html',{'publicacion': publicacion,'form': form,'user': _usuario, 'perfil': perfilesUsuario})

def editarpublicacion(request,pk):
	model = Publicacion
	form = PublicacionForm(request.POST)
	_idPublicacion = pk
	publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion).first()

	if request.user == publicacion.idUsuarioPublicacion:
		if request.method == 'POST':
			form = PublicacionForm(request.POST)
			tipoPublicacion = request.POST['tipoPublicacion']
			materia = request.POST['materia']
			estadoPublicacion = request.POST['estadoPublicacion']
			tituloPublicacion = request.POST['tituloPublicacion']
			precio = request.POST['precio']
			contenido = request.POST['contenido']
			publicacion.tipoPublicacion = tipoPublicacion
			publicacion.materia = materia
			publicacion.estadoPublicacion = estadoPublicacion
			publicacion.tituloPublicacion = tituloPublicacion
			publicacion.precio = precio
			publicacion.Contenido = contenido
			publicacion.save()
			return HttpResponseRedirect('/verpublicacion/%s' %pk  )
		else:
			usuario  = []
			_usuario = publicacion.idUsuarioPublicacion
			perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
			for _perfil in perfilesUsuario:
				usuario.append(Perfil.objects.all().last())

			return render(request, 'editarpublicacion.html',
			{'publicacion': publicacion,'form': form,'usuario': usuario, 'perfil': perfilesUsuario})
	else:
		return HttpResponseRedirect("/errorpage")

def portada(request):
	lista_publicacion = Publicacion.objects.all().distinct()
	myFilter = PublicacionFilter(request.GET, queryset=lista_publicacion)
	lista_publicacion=  myFilter.qs
	return render(request, "portada.html", {'lista_publicacion' : lista_publicacion,'Filter':myFilter})


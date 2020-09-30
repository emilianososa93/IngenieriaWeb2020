from django.shortcuts import render
from django.contrib.auth.decorators import login_required	

from .forms import PublicacionForm, CommentForm
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
		tituloPublicacion = request.POST['tituloPublicacion']
		precio = request.POST['precio']
		Contenido = request.POST['Contenido']
		idUsuarioPublicacion = request.user
		publicacion = Publicacion(
			tipoPublicacion = tipoPublicacion,
			tituloPublicacion = tituloPublicacion,
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


	return render(request, 'verpublicacion.html',{'publicacion': publicacion,'form': form,'usuario': usuario, 'perfil': perfilesUsuario})

def editarpublicacion(request,pk):
	model = Publicacion
	form = PublicacionForm(request.POST)
	_idPublicacion = pk
	publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion).first()

	if request.user == publicacion.idUsuarioPublicacion:
		if request.method == 'POST':
			form = PublicacionForm(request.POST)
			tipoPublicacion = request.POST['tipoPublicacion']
			tituloPublicacion = request.POST['tituloPublicacion']
			precio = request.POST['precio']
			contenido = request.POST['contenido']
			publicacion.tipoPublicacion = tipoPublicacion
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
	lista_publicacion = Publicacion.objects.all()
	return render(request, 'portada.html', {'lista_publicacion' : lista_publicacion})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/verpublicacion/%s' %pk  )
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
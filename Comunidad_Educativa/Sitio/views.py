from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .filters import PublicacionFilter
from .forms import PublicacionForm
from .models import Publicacion
from .models import SolicitudContacto
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
from django.core.mail import send_mail

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

@login_required
def verpublicacion(request,pk):
    form = PublicacionForm(request.POST)
    _idPublicacion = pk
    publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion).first()

    if request.method == 'POST':
        return HttpResponseRedirect('/verpublicacion/%s' %pk )
    else:
        usuario = []
        _usuario = publicacion.idUsuarioPublicacion
        perfilesUsuario = Perfil.objects.all().filter(usuario = _usuario)
        for _perfil in perfilesUsuario:
            usuario.append(Perfil.objects.all().last())
        solicitudexistente = []
        solicitudexistente = SolicitudContacto.objects.all().filter(idUsuarioSolicitante = request.user).filter(idUsuarioReceptor = _usuario)
        if not solicitudexistente:
            existesolicitud = False
        else:
            existesolicitud = True

        return render(request, 'verpublicacion.html',{'publicacion': publicacion,'form': form,'user': _usuario, 'perfil': perfilesUsuario, 'solicitud':existesolicitud })

@login_required
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

#FUNCIONALIDAD DE SOLICITAR DATOS DE CONTACTO
def solicitarcontacto(request,pk):
    solicitante = User.objects.all().filter(id = request.user.id).first()
    #por ahora solo un perfil - chequear
    perfil_solicitante = Perfil.objects.all().filter(usuario = request.user.id)

    _idPublicacion = pk
    publicacion = Publicacion.objects.all().filter(idPublicacion = _idPublicacion).first()

    _usuario = publicacion.idUsuarioPublicacion
    _email = _usuario.email


    email_subject   = 'Alguien quiere ponerse en contacto contigo! :)'
    #corregir link y contenido
    email_body      = "Hola %s! El usuario '%s' quiere ponerse en contacto contigo por tu publicación: https://comunidadeducativa.herokuapp.com/verpublicacion/%s. Puedes contactarlo por email o teléfono." % (_usuario.first_name, solicitante.username, pk)

    send_mail(email_subject,email_body, 'comunidadeducativaseia@gmail.com',[_email])


    model = SolicitudContacto

    solicitud = SolicitudContacto(
        idUsuarioSolicitante = request.user,
        idUsuarioReceptor = _usuario
    )

    solicitud.save()

    return HttpResponseRedirect('/verpublicacion/%s' %pk  )

def portada(request):
	lista_publicacion = Publicacion.objects.all().distinct()
	myFilter = PublicacionFilter(request.GET, queryset=lista_publicacion)
	lista_publicacion=  myFilter.qs
	return render(request, "portada.html", {'lista_publicacion' : lista_publicacion,'Filter':myFilter})


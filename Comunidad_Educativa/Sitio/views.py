from django.shortcuts import render
from django.contrib.auth.decorators import login_required	


@login_required
def nuevapublicacion(request):
	return render(request, 'nuevapublicacion.html')



def portada(request):
	return render(request, 'portada.html')
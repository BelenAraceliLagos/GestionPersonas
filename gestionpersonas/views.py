from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Persona
from .forms import PersonaForm

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def personas(request):
    busqueda = request.POST.get("buscar")
    personas = Persona.objects.all()

    if busqueda:
        personas = Persona.objects.filter(Q(nombre__icontains= busqueda) | Q(id__icontains= busqueda)).distinct()       

    return render(request, 'personas/index.html', {'personas': personas})

def crear(request):
    formulario = PersonaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('personas')
    return render(request, 'personas/crear.html', {'formulario': formulario})

def editar(request, id):
    persona = Persona.objects.get(id=id)
    formulario = PersonaForm(request.POST or None, request.FILES or None, instance=persona)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('personas')
    return render(request, 'personas/editar.html', {'formulario': formulario})

def eliminar(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('personas')


#def crear(request):
 #   return render(request, 'personas/crear.html')


# Create your views here.
from django.shortcuts import render, redirect
from .forms import CategoriaForm, AutorForm, PublicacionForm
from .models import Publicacion

def nueva_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nueva_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nueva Categoría'})

def nuevo_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_autor')
    else:
        form = AutorForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nuevo Autor'})

def nueva_publicacion(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nueva_publicacion')
    else:
        form = PublicacionForm()
    return render(request, 'blog/formulario.html', {'form': form, 'titulo': 'Nueva Publicación'})

def buscar_publicacion(request):
    publicaciones = []
    if request.method == "POST":
        termino = request.POST.get('termino')
        publicaciones = Publicacion.objects.filter(titulo__icontains=termino)
    return render(request, 'blog/buscar.html', {'publicaciones': publicaciones})

def inicio(request):
    return render(request, 'blog/inicio.html')

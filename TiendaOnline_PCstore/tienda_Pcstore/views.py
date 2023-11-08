from django.shortcuts import render, redirect, get_object_or_404

def contacto(request):  
    title = 'Django Course!!'
    return render(request, 'contacto.html', {
        "title": title
    })

# Create your views here.

def acercaDe(request):  # Cambia el nombre de la función a hacercaDe
    title = 'Django Course!!'
    return render(request, 'acercaDe.html', {
        "title": title
    })

def inicio(request):
    # Tu lógica de vista aquí
    return render(request, 'inicio.html')

def index(request):
    # Tu lógica de vista aquí
    return render(request, 'index.html')
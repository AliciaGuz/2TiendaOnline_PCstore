from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404


def inicio(request):
    # Tu lógica de vista aquí
    return render(request, 'inicio.html')

def hacerDe(request):
    title = 'Django Course!!'
    return render(request, 'hacercaDe.html', {
        "title":title
    })
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('hacercaDe/', views.hacercaDe, name='hacercaDe'),
    path('contacto/', views.contacto, )# Agregar el nombre 'hacercaDe' a la vista
    # Otros patrones URL aquí
]
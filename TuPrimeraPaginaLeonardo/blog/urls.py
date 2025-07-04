from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categoria/nueva/', views.nueva_categoria, name='nueva_categoria'),
    path('autor/nuevo/', views.nuevo_autor, name='nuevo_autor'),
    path('publicacion/nueva/', views.nueva_publicacion, name='nueva_publicacion'),
    path('publicacion/buscar/', views.buscar_publicacion, name='buscar_publicacion'),
]

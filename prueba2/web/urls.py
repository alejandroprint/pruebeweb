from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('Principal', views.Principal, name='Principal'),
    path('Notebook', views.Notebook, name='Notebook'),
    path('celulares', views.celulares, name='celulares'),
    path('Formulario', views.Formulario, name='Formulario'),
    path('agregar_p', views.agregar_p, name='agregar_p'),
    path('agregar_produc', views.agregar_produc, name='agregar_produc'),
    path('eliminar_p', views.eliminar_p, name='eliminar_p'),
    path('eliminar_porducto', views.eliminar_porducto, name='eliminar_porducto'),
    path('listado_producto', views.listado_producto, name='listado_producto'),
    path('editar', views.editar, name='editar'),
    path('buscar_para_editar', views.buscar_para_editar, name='buscar_para_editar'),
    path('actualizar_producto', views.actualizar_producto, name='actualizar_producto'),

]
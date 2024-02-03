
from django.urls import path
from AppParte import views
urlpatterns = [
    path('', views.index, name='index'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('parte_diario', views.parte_diario, name='parte_diario'),
    path('salir', views.salir, name='salir'),
    path('ingresar', views.ingresar, name='ingresar'),
    path('control', views.control, name='control'),
    path('controlModificar/<int:id>', views.controlModificar, name='controlModificar'),
    path('controlModificar/editarParte', views.editarParte, name='controlEditar'),
    path('controlEliminar/<int:id>', views.controlEliminar, name='controlEliminar'),
]
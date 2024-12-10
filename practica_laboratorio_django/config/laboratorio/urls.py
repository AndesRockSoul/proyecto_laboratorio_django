from django.urls import path
from .views import index, listar, crear, editar, eliminar,listar_laboratorios, editar_laboratorio,eliminar_laboratorio,crear_laboratorio

urlpatterns = [
    path('', index, name='index'),
    path('listar_productos/', listar, name='listar'),
    path('crear_producto/', crear, name='crear'),
    path('editar_producto/<int:producto_id>/', editar, name='editar'),
    path('eliminar_producto/<int:producto_id>/', eliminar, name='eliminar'),
    #path('buscar_producto/', buscar, name='buscar'),
    path('listar_laboratorios/',listar_laboratorios, name='listar_laboratorios'),
    path('editar_laboratorio/<int:laboratorio_id>', editar_laboratorio, name='editar_laboratorio'),
    path('eliminar_laboratorio/<int:laboratorio_id>', eliminar_laboratorio, name='eliminar_laboratorio'),
    path('crear_laboratorio/', crear_laboratorio, name='crear_laboratorio'),
]
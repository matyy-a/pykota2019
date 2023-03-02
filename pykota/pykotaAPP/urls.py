from django.urls import path
from django.urls import path, include
from . import views
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('impresora/lista/', views.impresora_lista, name='impresora_lista'),
	path('impresora/<int:pk>/editar', views.impresora_editar, name='impresora_editar'),
	path('impresora/<int:pk>/borrar', views.impresora_borrar, name='impresora_borrar'),

	path('grupo/lista/', views.grupo_lista, name='grupo_lista'),
	path('grupo/<int:pk>/editar', views.grupo_editar, name='grupo_editar'),
	path('grupo/<int:pk>/borrar', views.grupo_borrar, name='grupo_borrar'),

	path('grupo-usuario/lista/', views.grupousuario_lista, name='grupo-usuario_lista'),
	path('grupo-usuario/<int:pk>/editar', views.grupousuario_editar, name='grupousuario_editar'),
	path('grupo-usuario/<int:pk>/borrar', views.grupousuario_borrar, name='grupousuario_borrar'),

	path('usuario/lista', views.usuario_lista, name='usuario_lista'),
	path('usuario/<int:pk>/editar', views.usuario_editar, name='usuario_editar'),
	path('usuario/<int:pk>/borrar', views.usuario_borrar, name='usuario_borrar'),

	path('asignar-cuota/lista/', views.asignarcuota_lista, name='asignarcuota_lista'),
	path('asignar-cuota/<int:pk>/editar', views.asignarcuota_editar, name='asignarcuota_editar'),
	path('asignar-cuota/<int:pk>/borrar', views.asignarcuota_borrar, name='asignarcuota_borrar'),

]

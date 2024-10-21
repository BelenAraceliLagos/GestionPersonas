from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('personas', views.personas, name='personas'),
    path('personas/crear', views.crear, name='crear'),
    path('personas/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('personas/editar/<int:id>', views.editar, name='editar'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('rutas/', views.rutas, name='rutas'),
    path('aprovechamiento/', views.aprovechamiento, name='aprovechamiento'),
    path('contacto/', views.contacto, name='contacto'),
    path('pqrs/', views.pqrs, name='pqrs'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('mis-certificados/', views.mis_certificados, name='mis_certificados'),
]

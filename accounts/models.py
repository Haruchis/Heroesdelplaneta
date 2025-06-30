from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    es_aliado = models.BooleanField(default=True)  # True si es aliado, False si es admin/staff
    nombre_conjunto = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username


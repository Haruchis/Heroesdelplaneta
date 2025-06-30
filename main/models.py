from django.db import models

class DocumentoPublico(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    archivo = models.FileField(upload_to='documentos/')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

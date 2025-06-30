from django.contrib import admin
from .models import Certificado

class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'creado')
    search_fields = ('nombre', 'usuario__username')

admin.site.register(Certificado, CertificadoAdmin)

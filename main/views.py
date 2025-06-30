from django.shortcuts import render
from .models import DocumentoPublico
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def inicio(request):
    documentos = DocumentoPublico.objects.all()
    return render(request, 'main/inicio.html', {'documentos': documentos})
def rutas(request):
    return render(request, 'main/rutas.html')
def aprovechamiento(request):
    return render(request, 'main/aprovechamiento.html')
def contacto(request):
    return render(request, 'main/contacto.html')
def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        contenido = f"Nombre: {nombre}\nCorreo: {email}\n\nMensaje:\n{mensaje}"
        send_mail(
            asunto,
            contenido,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # o una lista de destinatarios
        )
        messages.success(request, '¡Tu mensaje ha sido enviado con éxito!')

    return render(request, 'main/contacto.html')
def pqrs(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        tipo = request.POST.get('tipo')
        mensaje = request.POST.get('mensaje')

        contenido = f"""
        Tipo de PQRS: {tipo}
        Nombre: {nombre}
        Email: {email}
        Mensaje: {mensaje}
        """

        send_mail(
            subject=f'PQRS - {tipo}',
            message=contenido,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
    
    return render(request, 'main/pqrs.html')
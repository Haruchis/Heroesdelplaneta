from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def documentos(request):
    return render(request, 'documentos/documentacion.html')

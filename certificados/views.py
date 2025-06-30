from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mis_certificados(request):
    certificados = request.user.certificados.all()
    return render(request, 'certificados/mis_certificados.html', {'certificados': certificados})

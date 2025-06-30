"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib import messages 
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from main import views as main_views
from documentos import views as documentos_views

class LogoutWithMessage(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Sesión cerrada correctamente.")
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutWithMessage.as_view(next_page='login'), name='logout'),
    path('documentacion/', include('documentos.urls')),
    path('', include('certificados.urls')),  # Ruta para certificados
    path('rutas/', main_views.rutas, name='rutas'),
    path('', include('main.urls')),
]


# Esto permite servir archivos como imágenes o certificados en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
class LogoutWithMessage(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Sesión cerrada correctamente.")
        return super().dispatch(request, *args, **kwargs)
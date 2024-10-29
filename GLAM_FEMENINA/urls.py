# mi_proyecto/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Inventario.urls')),  # Asegúrate de incluir las URLs de la app
]
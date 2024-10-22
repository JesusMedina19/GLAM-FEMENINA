from django.contrib import admin
from django.urls import path
from Inventario.views import register_view , login_view, hola_mundo_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola_mundo/', hola_mundo_view, name='hola_mundo'),
    path('registro/', register_view, name='registro'),
    path('',login_view, name='login'),  
]

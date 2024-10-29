from django.contrib import admin
from django.urls import path
from Inventario.views import register_view , login_view, menu_view,variedades_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name='login'),  
    path('menu/', menu_view, name='menu'),
    path('registro/', register_view, name='registro'),
    path('Variedades/', variedades_view, name='variedades')
]

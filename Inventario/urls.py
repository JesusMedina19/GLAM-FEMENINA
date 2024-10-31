from django.contrib import admin
from django.urls import path
from Inventario.views import (
    register_view,
    login_view,
    menu_view,
    variedades_view,
    productos_capilares_view,
    catalogo_uñas_view,
    catalogo_mayorista_view,
    catalogo_al_detal_view,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  
    path('menu/', menu_view, name='menu'),
    path('registro/', register_view, name='registro'),
    path('Variedades.html/', variedades_view, name='variedades'),
    path('productos-capilares/', productos_capilares_view, name='productos_capilares'),
    path('catalogo-unas/', catalogo_uñas_view, name='catalogo_uñas'),
    path('catalogo-mayorista/', catalogo_mayorista_view, name='catalogo_mayorista'),
    path('catalogo-al-detal/', catalogo_al_detal_view, name='catalogo_al_detal'),
    
]

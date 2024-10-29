from django.contrib import admin
from django.urls import path
from Inventario.views import register_view , login_view, menu_view,variedades_view
from Inventario.views import productos_capilares_view,catalogo_uñas_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name='login'),  
    path('menu/', menu_view, name='menu'),
    path('registro/', register_view, name='registro'),
    path('Variedades/', variedades_view, name='Variedades'),
    path('Productos Capilares/',productos_capilares_view, name='Productos Capilares' ),
    path('Catalogo Uñas/',catalogo_uñas_view,name='Catalogo de uñas')
]
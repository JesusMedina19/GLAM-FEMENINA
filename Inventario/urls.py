from django.contrib import admin
from django.urls import path
from . import views
from Inventario.views import (
    register_view,
    login_view,
    menu_view,

    
    

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  
    path('menu/', menu_view, name='menu'),
    path('registro/', register_view, name='registro'),
    path('agregar_producto/',views.agregar_producto,name='agregar_producto'),
    path('crear_categoria/',views.crear_categoria,name='crear_categoria'),
    path('categoria/',views.categorias,name='categorias'),
    path('categorias/modificar/<int:id_categoria>/', views.modificar_categoria, name='modificar_categoria'),
    path('categorias/eliminar/<int:id_categoria>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('categorias/<int:id_categoria>/', views.detalle_categoria, name='detalle_categoria'),
] 

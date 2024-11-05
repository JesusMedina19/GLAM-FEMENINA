from django.contrib import messages
from django.contrib.auth import  login
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from .forms import CustomUserCreationForm
from Inventario.models import Usuario 
from django.shortcuts import render, redirect
from .models import Categoria,Producto
from .forms import ProductoForm  # Asegúrate de tener un formulario para validar los datos


#Vista para ingresar a la aplicacion
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Usa get() para evitar el error
        password = request.POST.get('password')  # Usa get() para evitar el error
        
        if username and password:  # Asegúrate de que ambos campos no sean None
            try:
                user = Usuario.objects.get(usuario=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('menu')
                else:
                    messages.error(request, 'Datos incorrectos. Intenta nuevamente.')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuario no encontrado.')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')
    
    return render(request, 'login.html')


#Vista para registrar el usuario en la aplicaion
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito')
            return redirect('login')  # Redirige a la página de inicio de sesión
        else:
            messages.error(request, 'Error al crear la cuenta. Por favor, verifica los errores.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registro.html', {'form': form})


#Vista del menu de la aplicacion
def menu_view(request):
        categorias = Categoria.objects.all()
        return render(request,'menu.html',{'categorias':categorias})
        
        




def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            try:
                producto = form.save()  # Intenta guardar el producto
                messages.success(request, 'Producto agregado exitosamente.')
                return redirect('menu')  # Cambia esto por la vista correspondiente
            except Exception as e:
                messages.error(request, f'Ocurrió un error al guardar el producto: {e}')
                print(f"Error al guardar el producto: {e}")  # Imprimir el error en la consola
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
            print(form.errors)  # Imprimir errores de validación en la consola
    else:
        form = ProductoForm()
    
    return render(request, 'menu.html', {'form': form})  # Cambia la ruta del template

def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nueva_categoria = Categoria(nombre=nombre)
        nueva_categoria.save()
        return redirect('categorias') 
    
    categorias = Categoria.objects.all()
    return render(request,'categorias.html',{'categorias':categorias})

def categorias(request):
    categorias = Categoria.objects.all()  # Corregido "objects" en minúscula
    return render(request, 'categorias.html', {'categorias': categorias})


def modificar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria.nombre = nombre
        categoria.save()
        return redirect('categorias')
    return render(request, 'Inventario/modificar_categoria.html', {'categoria': categoria})


def eliminar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias')
    return render(request, 'Inventario/eliminar_categoria.html', {'categoria': categoria})

def detalle_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)  # Usa 'id_categoria' en lugar de 'id'
    productos = Producto.objects.filter(categoria_producto=categoria)  # Ajusta esto a tu modelo de relación

    context = {
        'categoria': categoria,
        'productos': productos,
    }
    
    return render(request, 'detalle_categoria.html', context)
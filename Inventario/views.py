from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from Inventario.models import Usuario  # Asegúrate de importar tu modelo User


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

def menu_view(request):
    return render(request, 'menu.html')  

def variedades_view(request):
    return render(request, 'variedades.html')  # Asegúrate de que este archivo exista

def productos_capilares_view(request):
    return render(request, 'productos_capilares.html')  # Asegúrate de que este archivo exista

def catalogo_unas_view(request):
    return render(request, 'catalogo_unas.html')  # Asegúrate de que este archivo exista

def catalogo_mayorista_view(request):
    return render(request, 'catalogo_mayorista.html')  # Asegúrate de que este archivo exista

def catalogo_al_detalle_view(request):
    return render(request, 'catalogo_al_detalle.html')  # Asegúrate de que este archivo exista

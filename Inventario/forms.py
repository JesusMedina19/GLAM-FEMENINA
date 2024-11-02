from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Producto # Asegúrate de que esto apunta a tu modelo correcto


#Formulario para agregar usuarios 
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('usuario', 'nombre', 'password1', 'password2')  # Asegúrate de que estos coincidan con tu modelo

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


#Formulario para agregar producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','descripcion','cantidad','imagen']
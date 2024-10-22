from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario  # Asegúrate de que esto apunta a tu modelo correcto

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('usuario', 'nombre', 'password1', 'password2')  # Asegúrate de que estos coincidan con tu modelo

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

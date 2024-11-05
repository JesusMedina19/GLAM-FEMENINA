from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager,BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, contrasena=None, **extra_fields):
        if not usuario:
            raise ValueError('El nombre de usuario debe ser proporcionado')
        usuario = self.model(usuario=usuario, **extra_fields)
        usuario.set_password(contrasena)  # Usa set_password para guardar la contraseña
        usuario.save(using=self._db)
    def create_superuser(self, usuario, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(usuario, contrasena, **extra_fields)

#-----------------------------------
# Modelo de usuario
class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    rol = models.CharField(max_length=15, default="empleado")
    usuario = models.CharField(max_length=50, unique=True)
    #contrasena = models.CharField(max_length=128)

    objects = UsuarioManager()  # Asegúrate de usar UsuarioManager aquí
    USERNAME_FIELD = 'usuario' 
    REQUIRED_FIELDS = ['nombre']  # Puedes agregar otros campos requeridos si lo deseas
    
    def __str__(self):
        return self.usuario


#Modelo de cliente   
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 30)
    correo = models.EmailField(max_length = 150)
    direccion = models.CharField(max_length = 150)
    telefono = PhoneNumberField()

    
    def __str__(self):
        return self.nombre


#Modelo de Categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nombre
    
    
    
#Modelo de Producto    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 30)
    precio = models.DecimalField(max_digits = 10,
                                decimal_places = 2)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to = 'productos/',
                                null= True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Precio: {self.precio}, " \
            f"Descripcion: {self.descripcion}, "\
            f"Disponible: {self.disponible}"



#Modelo de Producto_Categoria
class Categoria_Producto(models.Model):
    id_categoria_cliente = models.AutoField(primary_key = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.categoria.nombre} / {self.producto.nombre}"



#Modelo de ventas
class Venta(models.Model):
    id_venta = models.AutoField(primary_key = True)
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.DecimalField(max_digits = 10 , 
                                decimal_places = 2 )
    
    def __str__(self) -> str:  
        return f"Date: {self.fecha}, Total: {self.total}"

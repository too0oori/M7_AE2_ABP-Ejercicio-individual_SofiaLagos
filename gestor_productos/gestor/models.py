from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    stock = models.PositiveIntegerField(blank=False)
    descripcion = models.TextField(blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    class Meta :
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
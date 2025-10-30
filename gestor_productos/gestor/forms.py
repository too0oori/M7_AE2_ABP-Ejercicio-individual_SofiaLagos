from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción del Producto',
            'precio': 'Precio del Producto',
            'stock': 'Stock del Producto',
            'fecha_creacion': 'Fecha de Creación',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_creacion': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }
    
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # CRÍTICO: Excluye fecha_creacion porque es auto_now_add
        fields = ['nombre', 'descripcion', 'precio', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'required': True
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01',
                'min': '0',
                'required': True
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': '0',
                'required': True
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Si estamos editando un producto existente
        if self.instance and self.instance.pk:
            # Agregar los valores actuales como placeholders
            self.fields['nombre'].widget.attrs['placeholder'] = f'Actual: {self.instance.nombre}'
            self.fields['precio'].widget.attrs['placeholder'] = f'Actual: ${self.instance.precio}'
            self.fields['stock'].widget.attrs['placeholder'] = f'Actual: {self.instance.stock} unidades'
            self.fields['descripcion'].widget.attrs['placeholder'] = f'Actual: {self.instance.descripcion[:100]}...'
        else:
            # Si estamos creando un producto nuevo
            self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre del producto'
            self.fields['precio'].widget.attrs['placeholder'] = 'Ej: 999.99'
            self.fields['stock'].widget.attrs['placeholder'] = 'Cantidad disponible'
            self.fields['descripcion'].widget.attrs['placeholder'] = 'Descripción detallada del producto'
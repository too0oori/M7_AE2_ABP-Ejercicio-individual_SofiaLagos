from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista
    list_display = ('id', 'nombre', 'precio', 'stock', 'fecha_creacion')
    
    # Campos por los que se puede buscar
    search_fields = ('nombre', 'descripcion')
    
    # Filtros laterales
    list_filter = ('fecha_creacion', 'stock')
    
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion',)
    
    # Campos editables en la lista (opcional, pero útil)
    list_editable = ('precio', 'stock')
    
    # Organización del formulario
    fieldsets = (
        ('Información del Producto', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Detalles Comerciales', {
            'fields': ('precio', 'stock')
        }),
    )
    
    # Permite editar directamente desde la lista
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si estamos editando
            return self.readonly_fields
        return []
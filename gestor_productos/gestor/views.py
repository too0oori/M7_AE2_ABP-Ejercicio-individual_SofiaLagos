from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Producto
from django.shortcuts import get_object_or_404
from .forms import ProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '¡Te has registrado correctamente!')
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def view_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

# Vista para LOGIN (maneja la autenticación)
def login_view(request):
    # Si viene redirigido por @login_required, mostrar mensaje
    if 'next' in request.GET:
        messages.warning(request, 'Debes iniciar sesión para acceder a esta página.')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # ← authenticate, no user.authenticate
        if user is not None:
            login(request, user)
            next_page = request.GET.get('next', 'home')
            return redirect(next_page)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@permission_required('gestor.add_producto', raise_exception=True)
def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El producto se ha agregado correctamente!')
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'add_producto.html', {'form': form})

@permission_required('gestor.delete_producto', raise_exception=True)
def delete_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, '¡El producto se ha eliminado correctamente!')
        return redirect('productos')
    
    return render(request, 'delete_producto.html', {'producto': producto})

@permission_required('gestor.change_producto', raise_exception=True)
def edit_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El producto se ha editado correctamente!')
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'edit_producto.html', {'form': form})
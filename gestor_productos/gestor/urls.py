from django.contrib import admin
from django.urls import path
from gestor import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('productos/', views.view_productos, name='productos'),
    path('productos/add/', views.add_producto, name='add_producto'),
    path('productos/edit/<int:producto_id>/', views.edit_producto, name='edit_producto'),
    path('productos/delete/<int:producto_id>/', views.delete_producto, name='delete_producto'),
]
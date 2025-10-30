# 🛒 Gestor de Productos — Módulo 6 (ABP Individual)

Este proyecto corresponde al **Ejercicio Individual AE6_ABP del Módulo 6 del Bootcamp Full Stack Python**.  
Se trata de una **plataforma de gestión de productos** desarrollada con **Django**, que permite crear, editar y eliminar productos desde el **panel administrativo** o mediante vistas protegidas por permisos y roles de usuario.

---

## 🚀 Características principales

- **Sistema de autenticación** (registro, login, logout).
- **Gestión de productos** con modelo `Producto` (nombre, descripción, precio, stock, fecha de creación).
- **Panel administrativo de Django** completamente personalizado.
- **Permisos y roles** configurables (Administradores, Gestores, Usuarios).
- **Interfaz Bootstrap 5** con mensajes dinámicos y control de acceso.

---

## ⚙️ Instalación y ejecución


# Clonar el repositorio
```bash
git clone https://github.com/too0oori/M6_AE6_ABP-Ejercicio-individual
cd M6_AE6_ABP-Ejercicio-individual
```

# Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # En macOS/Linux
venv\Scripts\activate      # En Windows
```

# Instalar dependencias
```bash
pip install -r requirements.txt
```

# Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

# Crear superusuario
```
python manage.py createsuperuser
```

# Ejecutar servidor
```bash
python manage.py runserver
```

## 🧩 Roles y permisos

| Grupo                 | Permisos                             |
| --------------------- | ------------------------------------ |
| **Administradores**   | Agregar, editar y eliminar productos |
| **Gestores**          | Agregar y editar productos           |
| **Cliente**           | Solo pueden visualizar productos     |

## 🗂️ Estructura básica
```bash
gestor_productos/
│
├── gestor/
│   ├── models.py          # Modelo Producto
│   ├── views.py           # Vistas con control de permisos
│   ├── admin.py           # Configuración del panel admin
│   ├── forms.py           # Formulario ProductoForm
│   ├── templates/         # Templates base y CRUD
│
├── gestor_productos/
│   ├── settings.py        # Configuración general
│   ├── urls.py            # Rutas principales
│
└── db.sqlite3             # Base de datos SQLite
```
## 👩‍💻 Desarrollado por

Sofía Lagos
Bootcamp Desarrollo Full Stack Python – Módulo 6
Chile · 2025

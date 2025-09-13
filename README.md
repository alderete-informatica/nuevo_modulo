# Simple Menu - Módulo Odoo

Este es un módulo de prueba para **Odoo**, llamado `simple_menu`, que agrega un menú con dos opciones:  
- **Nuevo**: muestra un mensaje de bienvenida.  
- **Acerca de**: muestra información del autor y empresa.  

## 👤 Autor
- **Nombre:** Alderete Lucas Alberto  
- **Empresa:** ALDERETE INFORMÁTICA Y SOPORTE  

---

## 🚀 Instalación en Odoo.sh

### 1. Crear un proyecto en Odoo.sh
1. Acceder a [https://www.odoo.sh/projects](https://www.odoo.sh/projects).  
2. Hacer clic en **New Project**.  
3. Conectar la cuenta de GitHub (si no está conectada).  
4. Seleccionar este repositorio:  
   ```
   https://github.com/alderete-informatica/nuevo_modulo.git
   ```
5. Usar la branch **main** (es la que contiene el módulo).  

---

### 2. Compilar la Build
- Odoo.sh descargará el repositorio y levantará el entorno.  
- Esperar a que finalice la build.  

---

### 3. Instalar el módulo en Odoo
1. Ingresar al entorno del proyecto.  
2. Activar **Modo Desarrollador** (en Configuración > Activar modo desarrollador).  
3. Ir a **Aplicaciones > Actualizar lista de aplicaciones**.  
4. Buscar **Simple Menu**.  
5. Hacer clic en **Instalar**.  

---

## 📂 Estructura del repositorio
```
nuevo_modulo/
├── simple_menu/
│   ├── __manifest__.py
│   ├── __init__.py
│   ├── models/
│   ├── views/
```

---

## 📌 Notas
- Este repositorio contiene únicamente el módulo `simple_menu`.  
- Para proyectos más grandes, se recomienda agrupar varios módulos dentro de la misma carpeta de repositorio.  

---

## 👤 Autor
- **Nombre:** Alderete Lucas Alberto  
- **Empresa:** ALDERETE INFORMÁTICA Y SOPORTE  

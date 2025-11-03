# 🧾 Sistema de Registro de Vendedores y Productos (Python)

Este programa permite **registrar vendedores con sus productos, consultar información y generar reportes** sobre inventarios y ventas.  
Fue desarrollado en **Python puro**, sin necesidad de librerías externas.

---

## 📦 Funcionalidades

### 🔹 Inciso A: Registrar vendedores y productos
Permite ingresar la información de un nuevo vendedor junto con los productos que ofrece.  
Cada vendedor se almacena en una lista global (`VENDEDORES`) con su propio inventario.

### 🔹 Inciso B: Mostrar todos los vendedores
Muestra un listado completo de todos los vendedores registrados, junto con sus productos e inventarios.

### 🔹 Inciso C: Buscar un vendedor específico
Permite buscar un vendedor por su código y mostrar todos sus datos personales y productos.

### 🔹 Inciso D: Mostrar productos vendidos
Genera un reporte detallado de los productos vendidos por un vendedor y calcula el total de ventas.

---

## 🧠 Estructura de Datos

```python
VENDEDORES = [
    {
        "código": 1,
        "nombre": "Juan",
        "apellido": "Pérez",
        "direccion": "Ciudad",
        "dpi": "1234567890101",
        "productos": [
            {
                "nombre": "Camisa",
                "inventario": 10,
                "vendidos": 3,
                "precio_unitario": 75.50
            }
        ],
        "total_inventario": 755.00
    }
]
```

---

## ▶️ Ejecución

Ejecuta el archivo principal desde consola o cualquier entorno Python:

```bash
python main.py
```

---

## 📋 Menú Principal

```text
##############################################
          📋 SISTEMA DE REGISTRO DE VENTAS
##############################################
1. ➕ Registrar nuevos vendedores y productos (Inciso A)
2. 📋 Mostrar todos los vendedores (Inciso B)
3. 🔍 Mostrar datos de un vendedor específico (Inciso C)
4. 💰 Mostrar productos vendidos de un vendedor (Inciso D)
5. 🚪 Salir
##############################################
```

---

## 🧑‍💻 Autor
Proyecto educativo de ejemplo en Python.
Puedes modificarlo libremente para tus propias prácticas o portafolio.

---

## 🪶 Licencia
Este proyecto se distribuye bajo la licencia **MIT**.

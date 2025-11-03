# =================================================================
# ESTRUCTURA DE DATOS GLOBAL
# VENDEDORES será una lista de diccionarios, donde cada diccionario
# representa un vendedor y contiene una lista de diccionarios para sus productos.
# =================================================================
VENDEDORES = []
CODIGO_ACTUAL = 1 # Contador para asignar códigos automáticamente

# =================================================================
# FUNCIONES AUXILIARES
# =================================================================

def buscar_vendedor(codigo):
    """Busca y retorna un vendedor por su código, o None si no lo encuentra."""
    for vendedor in VENDEDORES:
        if vendedor['código'] == codigo:
            return vendedor
    return None

def calcular_total_inventario(productos):
    """Calcula el valor total del inventario de un vendedor."""
    total = 0.0
    for p in productos:
        total += p['inventario'] * p['precio_unitario']
    return total

# =================================================================
# INCISO A: Registrar “N” vendedores con sus respectivos productos
# =================================================================
def registrar_vendedores():
    """Permite registrar un nuevo vendedor y sus productos."""
    global CODIGO_ACTUAL
    print("\n" + "="*50)
    print("        ➕ REGISTRO DE NUEVO VENDEDOR")
    print("="*50)
    
    # 1. Datos Personales del Vendedor
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    direccion = input("Ingrese Dirección: ")
    dpi = input("Ingrese DPI: ")

    # Estructura del nuevo vendedor
    nuevo_vendedor = {
        'código': CODIGO_ACTUAL,
        'nombre': nombre,
        'apellido': apellido,
        'direccion': direccion,
        'dpi': dpi,
        'productos': [], # Lista de diccionarios de productos
        'total_inventario': 0.0
    }
    
    # 2. Registro de Productos
    while True:
        print("\n--- Registro de Producto ---")
        nombre_articulo = input("Nombre del artículo (o 'fin' para terminar): ")
        if nombre_articulo.lower() == 'fin':
            break

        try:
            inventario = int(input("Número de artículos en inventario: "))
            precio_unitario = float(input("Precio de cada uno (Q): "))
            
            # Se inicializa 'vendidos' en 0 al momento del registro
            nuevo_producto = {
                'nombre': nombre_articulo,
                'inventario': inventario,
                'vendidos': 0, # Inicialmente no hay ventas
                'precio_unitario': precio_unitario
            }
            nuevo_vendedor['productos'].append(nuevo_producto)
            print("✅ Producto registrado.")
            
        except ValueError:
            print("❌ Error: Inventario y Precio deben ser números válidos.")

    # 3. Cálculo y Almacenamiento
    nuevo_vendedor['total_inventario'] = calcular_total_inventario(nuevo_vendedor['productos'])
    VENDEDORES.append(nuevo_vendedor)
    print(f"\n✨ Vendedor {nombre} {apellido} registrado con éxito. Código: {CODIGO_ACTUAL}")
    CODIGO_ACTUAL += 1

# =================================================================
# INCISO B: Mostrar todos los vendedores con todos sus datos y productos
# (Esta función fue provista por el usuario y se deja aquí para la integridad)
# =================================================================
def mostrar_todos_vendedores():
    """Muestra la información completa de cada vendedor registrado."""
    print("\n" + "="*50)
    print("          📋 REPORTE DE TODOS LOS VENDEDORES")
    print("="*50)
    
    if not VENDEDORES:
        print("No hay vendedores registrados.")
        return

    for vendedor in VENDEDORES:
        # Datos personales
        print(f"\nCódigo: **{vendedor['código']}**")
        print(f"Nombre: {vendedor['nombre']} {vendedor['apellido']}")
        print(f"Dirección: {vendedor['direccion']}")
        print(f"DPI: {vendedor['dpi']}")
        print(f"Valor Total de Inventario: Q{vendedor.get('total_inventario', 0.00):.2f}")
        
        # Datos de productos
        print("\n  --- Productos en Venta ---")
        if vendedor['productos']:
            # Se añade 'Cant. Vendida' al formato para ser más informativo en este reporte
            print("  | Artículo             | Inv. Total | Inv. Vendido | Inv. Restante | Precio Unitario |")
            print("  |----------------------|------------|--------------|---------------|-----------------|")
            
            for p in vendedor['productos']:
                # Calcular artículos que quedan
                articulos_quedan = p['inventario'] - p['vendidos']
                
                print(f"  | {p['nombre'][:20]:<20} | {p['inventario']:<10} | {p['vendidos']:<12} | {articulos_quedan:<13} | Q{p['precio_unitario']:<12.2f} |")
        else:
            print("  No tiene productos registrados.")
            
        print("-" * 50)


# =================================================================
# INCISO C: Mostrar los datos de un vendedor específico
# (Esta función fue provista por el usuario y se deja aquí para la integridad)
# =================================================================
def mostrar_vendedor_especifico():
    """Pide un código y muestra la información completa del vendedor."""
    print("\n" + "="*50)
    print("        🔍 BÚSQUEDA DE VENDEDOR POR CÓDIGO")
    print("="*50)
    
    try:
        codigo_buscado = int(input("Ingrese el número de código del vendedor: "))
    except ValueError:
        print("Error: El código debe ser un número entero.")
        return

    vendedor_encontrado = buscar_vendedor(codigo_buscado)
            
    if vendedor_encontrado:
        v = vendedor_encontrado
        print("\n--- Datos Personales ---")
        print(f"Código: **{v['código']}**")
        print(f"Nombre: {v['nombre']} {v['apellido']}")
        print(f"Dirección: {v['direccion']}")
        print(f"DPI: {v['dpi']}")
        print(f"Valor Total de Inventario: Q{v.get('total_inventario', 0.00):.2f}")
        
        # Datos de productos
        print("\n--- Productos en Venta ---")
        if v['productos']:
            print("  | Artículo             | Cant. Vendida | Cant. Queda | Precio Unitario |")
            print("  |----------------------|---------------|-------------|-----------------|")
            
            for p in v['productos']:
                articulos_quedan = p['inventario'] - p['vendidos']
                print(f"  | {p['nombre'][:20]:<20} | {p['vendidos']:<13} | {articulos_quedan:<11} | Q{p['precio_unitario']:<12.2f} |")
        else:
            print("  Vendedor sin productos registrados.")
            
    else:
        print(f"\n❌ Error: No se encontró ningún vendedor con el código {codigo_buscado}.")


# =================================================================
# INCISO D: Mostrar los productos vendidos de un vendedor específico
# =================================================================
def mostrar_productos_vendidos():
    """Muestra el detalle de ventas y el total de un vendedor específico."""
    print("\n" + "="*50)
    print("         💰 REPORTE DE VENTAS POR VENDEDOR")
    print("="*50)
    
    try:
        codigo_buscado = int(input("Ingrese el número de código del vendedor: "))
    except ValueError:
        print("Error: El código debe ser un número entero.")
        return

    vendedor = buscar_vendedor(codigo_buscado)
    
    if not vendedor:
        print(f"\n❌ Error: No se encontró ningún vendedor con el código {codigo_buscado}.")
        return

    print(f"\n--- Ventas de {vendedor['nombre']} {vendedor['apellido']} (Código: {vendedor['código']}) ---")
    
    total_ventas = 0.0
    productos_vendidos = [p for p in vendedor['productos'] if p['vendidos'] > 0]
    
    if productos_vendidos:
        print("  | Artículo             | Cantidad | Precio Venta | Subtotal |")
        print("  |----------------------|----------|--------------|----------|")
        
        for p in productos_vendidos:
            cantidad = p['vendidos']
            precio_venta = p['precio_unitario'] # Usamos el precio unitario como precio de venta
            subtotal = cantidad * precio_venta
            total_ventas += subtotal
            
            print(f"  | {p['nombre'][:20]:<20} | {cantidad:<8} | Q{precio_venta:<10.2f} | Q{subtotal:<7.2f} |")
        
        print("  " + "-"*50)
        print(f"  **TOTAL DE VENTAS: Q{total_ventas:.2f}**")
    else:
        print("Este vendedor aún no registra productos vendidos.")

# =================================================================
# FUNCIÓN PRINCIPAL Y MENÚ
# =================================================================

def menu_principal():
    """Función principal que implementa el menú de opciones."""
    while True:
        print("\n\n" + "#"*50)
        print("              📋 SISTEMA DE REGISTRO DE VENTAS")
        print("#"*50)
        print("1. ➕ Registrar nuevos vendedores y productos (Inciso A)")
        print("2. 📋 Mostrar todos los vendedores (Inciso B)")
        print("3. 🔍 Mostrar datos de un vendedor específico (Inciso C)")
        print("4. 💰 Mostrar productos vendidos de un vendedor (Inciso D)")
        print("5. 🚪 Salir")
        print("#"*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_vendedores()
        elif opcion == '2':
            mostrar_todos_vendedores()
        elif opcion == '3':
            mostrar_vendedor_especifico()
        elif opcion == '4':
            mostrar_productos_vendidos()
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("\n❌ Opción no válida. Intente de nuevo.")

# Inicializar el programa
if __name__ == "__main__":
     menu_principal()
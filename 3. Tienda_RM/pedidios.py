# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------

# Lista para almacenar los productos
productos = []


# Función para mostrar el menú
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")


# Función para validar entrada de texto no vacía
def entrada_valida(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print("❌ Entrada inválida. No puede estar vacía.")

# Función para agregar un producto
def agregar_producto():
    producto = entrada_valida("Ingrese el nombre del producto a agregar: ")
    productos.append(producto)
    print(f"✅ Producto '{producto}' agregado correctamente.")

# Función para visualizar productos
def visualizar_productos():
    if not productos:
        print("📭 No hay productos en la lista.")
    else:
        print("\n📦 Lista de productos:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto}")

# Función para buscar un producto
def buscar_producto():
    nombre = entrada_valida("Ingrese el nombre del producto a buscar: ")
    if nombre in productos:
        print(f"🔍 Producto '{nombre}' encontrado en la lista.")
    else:
        print(f"❌ Producto '{nombre}' no encontrado.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = entrada_valida("Ingrese el nombre del producto a eliminar: ")
    if nombre in productos:
        productos.remove(nombre)
        print(f"🗑️ Producto '{nombre}' eliminado.")
    else:
        print(f"❌ Producto '{nombre}' no existe en la lista.")


# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = entrada_valida("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        visualizar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida. Ingrese un número del 1 al 5.")

# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------

# Lista para almacenar los productos
productos = []

# Bucle principal
while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    # Validar opción del menú
    if not opcion.isdigit() or int(opcion) not in range(1, 6):
        print("Opción inválida. Por favor, ingresa un número del 1 al 5.")
        continue

    opcion = int(opcion)

    # Opción 1: Agregar producto
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre del producto: ").strip()

        # Ingresar y validar precio
        while True:
            precio_input = input("Ingrese el precio del producto: ").strip()
            try:
                precio = float(precio_input)
                if precio <= 0:
                    print("El precio debe ser mayor a cero.")
                else:
                    break
            except ValueError:
                print("Precio inválido. Debe ser un número.")

        # Ingresar y validar cantidad
        while True:
            cantidad_input = input("Ingrese la cantidad del producto: ").strip()
            if cantidad_input.isdigit():
                cantidad = int(cantidad_input)
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser mayor a cero.")
            else:
                print("Cantidad inválida. Debe ser un número entero positivo.")

        # Crear diccionario y agregar a la lista
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(producto)
        print(f"Producto '{nombre}' agregado correctamente.")

    # Opción 2: Visualizar productos
    elif opcion == 2:
        if len(productos) == 0:
            print("No hay productos para mostrar.")
        else:
            print("\n--- Lista de productos ---")
            for i in range(len(productos)):
                p = productos[i]
                print(
                    f"{i + 1}. {p['nombre']} - Precio: ${p['precio']} - Cantidad: {p['cantidad']}"
                )

    # Opción 3: Buscar producto
    elif opcion == 3:
        buscar = input("Ingrese el nombre del producto a buscar: ").strip()
        while buscar == "":
            print("El nombre no puede estar vacío.")
            buscar = input("Ingrese el nombre del producto a buscar: ").strip()

        encontrado = False
        for p in productos:
            if p["nombre"].lower() == buscar.lower():
                print(
                    f"Producto encontrado: {p['nombre']} - Precio: ${p['precio']} - Cantidad: {p['cantidad']}"
                )
                encontrado = True
                break

        if not encontrado:
            print(f"Producto '{buscar}' no encontrado.")

    # Opción 4: Eliminar producto
    elif opcion == 4:
        eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()
        while eliminar == "":
            print("El nombre no puede estar vacío.")
            eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()

        eliminado = False
        for i in range(len(productos)):
            if productos[i]["nombre"].lower() == eliminar.lower():
                del productos[i]
                print(f"Producto '{eliminar}' eliminado correctamente.")
                eliminado = True
                break

        if not eliminado:
            print(f"Producto '{eliminar}' no encontrado en la lista.")

    # Opción 5: Salir
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break

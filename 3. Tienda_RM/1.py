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
        productos.append(nombre)
        print(f"Producto '{nombre}' agregado correctamente.")

    # Opción 2: Visualizar productos
    elif opcion == 2:
        if len(productos) == 0:
            print("No hay productos para mostrar.")
        else:
            print("\n--- Lista de productos ---")
            for i in range(len(productos)):
                print(f"{i + 1}. {productos[i]}")

    # Opción 3: Buscar producto
    elif opcion == 3:
        buscar = input("Ingrese el nombre del producto a buscar: ").strip()
        while buscar == "":
            print("El nombre no puede estar vacío.")
            buscar = input("Ingrese el nombre del producto a buscar: ").strip()

        encontrado = False
        for producto in productos:
            if producto.lower() == buscar.lower():
                encontrado = True
                break

        if encontrado:
            print(f"Producto '{buscar}' encontrado en la lista.")
        else:
            print(f"Producto '{buscar}' no encontrado.")

    # Opción 4: Eliminar producto
    elif opcion == 4:
        eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()
        while eliminar == "":
            print("El nombre no puede estar vacío.")
            eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()

        if eliminar in productos:
            productos.remove(eliminar)
            print(f"Producto '{eliminar}' eliminado correctamente.")
        else:
            print(f"Producto '{eliminar}' no encontrado en la lista.")

    # Opción 5: Salir
    elif opcion == 5:
        print("Saliendo del programa. ¡Hasta luego!")
        break

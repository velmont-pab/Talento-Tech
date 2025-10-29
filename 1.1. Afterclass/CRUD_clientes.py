# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------CRUD DE CLIENTES--------------------------------------

#lista vacía
clientes = []

while True:
    print("="*(30)+"MENÚ DE CLIENTES"+"="*(30))
    print("1. Agregar cliente") # C - create
    print("2. Mostrar clientes") # R - read
    print("3. Buscar cliente por nombre")
    print("4. Eliminar cliente")
    print("5. Buscar cliente con inicial específica")
    print("6. Buscar el cliente con el nombre más largo.")
    print("7. Salir")
    opcion = input("Elegí una opción: ").strip()
    # ============== Alta de clientes
    if opcion == '1':
        print("Alta de clientes")
        #validar nombre
        nombre = input("Nombre del cliente: ").strip().title()
        while nombre == '':
            print("❌ El nombre no debe ser vacío")
            nombre = input("Nombre del cliente: ").strip().title()
        #validar dni
        dni = input("DNI: ").strip()
        while not dni.isdigit() or len(dni) < 7 or len(dni) > 8:
            print("❌ Ingresa sólo números, entre 7 y 8 dígitos.")
            dni = input("DNI: ").strip()
        #validar teléfono
        telefono = input("Teléfono: ").strip()
        while not telefono.isdigit() or len(telefono) < 8:
            print("❌ Ingresa sólo números, al menos 8 dígitos.")
            telefono = input("Teléfono: ").strip()
        #validar email: contenga @ y punto
        email = input("Email: ").strip().lower()
        while '@' not in email or '.' not in email:
            print("El mail debe contener @ y un dominio válido.")
            email = input("Email: ").strip().lower()
        
        cliente = [nombre, int(dni), int(telefono), email]
        clientes.append(cliente)
        
        print("✔ Cliente agregado con éxito!")
    # ============== Listado de clientes    
    elif opcion == '2':
        if len(clientes) == 0: #presentamos el caso de lista vacía
            print("No hay clientes registrados.")
        else:
            print("Listado de clientes")
            #encabezado
            print("-"*70)
            print(f"{'N°':<4}{'NOMBRE':<20}{'DNI':<12}{'TELÉFONO':<15}{'EMAIL':<20}")
            print("-"*70)
            for i, cliente in enumerate(clientes, 1):
                #print(f"{i}. {cliente[0]} - DNI: {cliente[1]} - Tel.: {cliente[2]} - email: {cliente[3]}")
                print(f"{i:<4}{cliente[0]:<20}{cliente[1]:<12}{cliente[2]:<15}{cliente[3]:<20}")
            print("-"*70)
            print(f"Total de clientes: {len(clientes)}")
    # ============== Búsqueda de clientes
    elif opcion == '3':
        if len(clientes) == 0: #presentamos el caso de lista vacía
            print("No hay clientes registrados.")
        else:
            print("Buscar cliente por nombre:")
            buscar = input("Ingrese nombre del cliente a buscar: ").strip().lower()
            encontrado = False
            for cliente in clientes:
                if buscar == cliente[0].lower():
                    print(f"Encontrado: {cliente[0]} - DNI: {cliente[1]} - Tel.: {cliente[2]} - email: {cliente[3]}")
                    encontrado = True #opcional si solo busca una coincidencia, usar el break
            if not encontrado:
                print(f"No se encontraron resultados para la búsqueda: {buscar.title()}")           
    
    # ============== Eliminación de clientes            
    elif opcion == '4':
        if len(clientes) == 0: #presentamos el caso de lista vacía
            print("No hay clientes registrados.")
        else:
            print("Eliminar cliente")
            print("-"*70)
            print(f"{'N°':<4}{'NOMBRE':<20}{'DNI':<12}{'TELÉFONO':<15}{'EMAIL':<20}")
            print("-"*70)
            for i, cliente in enumerate(clientes, 1):
                print(f"{i:<4}{cliente[0]:<20}{cliente[1]:<12}{cliente[2]:<15}{cliente[3]:<20}")
            print("-"*70)
            while True:
                posicion = input("Ingresa el nro del cliente a eliminar: ").strip()
                if posicion.isdigit():
                    posicion = int(posicion) 
                    if 1 <= posicion <= len(clientes):
                        eliminado = clientes.pop(posicion-1) 
                        print(f"✔ Cliente {eliminado[0]} eliminado correctamente!") 
                        break
                    else:
                        print("❌ Número fuera de rango.")   
                else:
                    print("❌ Debe ingresar un número")    
    # ========= Filtrar por inicial
    elif opcion == '5':
        #validar que la lista no esté vacía
        letra = input("Ingresa letra para filtrar nombres: ").strip().lower()
        encontrados = 0
        for cliente in clientes:
            if cliente[0].lower().startswith(letra):
                print(f"{cliente[0]} - DNI: {cliente[1]} - Teléfono {cliente[2]} - Mail: {cliente[3]}")
                encontrados+=1
        if encontrados == 0:
            print(f"No se encontraron clientes que empiecen con {letra}")
        else:
            print(f"Cantidad de coincidencias con la letra {letra}: {encontrados}")
    # ======== cliente nombre más largo
    elif opcion == '6':
        #validar que la lista no esté vacía
        if len(clientes) > 0:
            mayor = clientes[0] # métodos de búsqueda, burbuja, mayor/menor
            for cliente in clientes:
                if len(cliente[0]) > len(mayor[0]):
                    mayor = cliente[0]
            print(f"El nombre más largo es: {mayor[0]} con {len(mayor[0])} caracteres.")
        else:
            print("No hay clientes registrados.")
    # ======== Salir
    elif opcion == '7':
        print(f"Cantidad de clientes cargados: {len(clientes)}")
        print("Fin del programa. ")
        break
    else:
        print("❌ Debe ingresar una opción válida")
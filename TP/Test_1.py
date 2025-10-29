# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------

ANCHO = 70
MARGEN = ("-" * ANCHO)
articulos=[]

"""-------------------------FUNCIONES--------------------------------------"""
# 1. funcion para cargar productos
def cargar_elementos(articulos) :
    """
    Añande elementos a la lista de articulos.
    
    Parámetros:
    Articulos (List): lista de productos vacia.
    """
    nuevo_item = input("Ingresa el nuevo producto: ").strip()
    descripcion_item = input("Detalle del producto: ").lower().strip()
    stock_item = int(input("Ingresa el Stock del producto: "))
  
    if nuevo_item == "" or len(nuevo_item) <= 3 :
        print(f"El nombre {nuevo_item} no es valido.\n#Recuerda que el nombre no debe estar vacio o contener menos de 3 letras")
        return
    
    elif descripcion_item == "" :
        while descripcion_item == "" :
            print("Parece que hubo un problema.".center(ANCHO))
            stock_item = input(f"Por Favor ingresa la descripcion de tus {nuevo_item.capitalize()} : ")

    elif stock_item == "" or stock_item <= 0 :
        while stock_item < 1 :
            print("Parece que hubo un problema.".center(ANCHO))
            stock_item = int(input(f"Por Favor ingresa la cantidad de {nuevo_item.capitalize()} {descripcion_item} : "))
    productos= [nuevo_item,descripcion_item,stock_item]
    articulos.append(productos)


# 2. funcion para ver productos
def ver_elementos(articulos):
    """
    Muestra los elementos de la lista de articulos.
    
    Parámetros:
    articulos(List): lista de productos cargada.


    """
    if not articulos:
        print("Todavia no has ingresado un producto")
        return
    for index,i in enumerate(articulos,start=1):
        nombre=i[0]
        descripcion=i[1]
        cantidad=i[2]
        print(f"Orden {index}: x{cantidad}u. {nombre} {descripcion}.")


#  3. funcion para Buscar productos
def buscar(articulos):
    """
    Busca productos en la lista de articulos.
    
    Parámetros:
    articulos(Lista): lista de productos cargada.
    
    """
    palabra=input("Dime, que es lo que buscas?\n").strip().lower()
    coincidencias=[]
    for i in articulos:
        if palabra in i[0] or palabra in i[1]:
            coincidencias.append(i)
    if coincidencias:
        print(f"Encontré {len(coincidencias)} producto/s:")
        for j in coincidencias:
            print(f"{j[0]} {j[1]} x{j[2]}u")
    else:
        print("no pude encontrar nada con esa palabra...Lo siento (┬┬﹏┬┬)")


# 4. funcion para Borrar productos
def borrar_elementos(articulos):
    """
    Elimina un elemento de la lista de articulos.

    Parámetros:
    articulos(List): lista de productos cargada.
    """
    if not articulos:
        print("debes agregar algun producto para eliminar".center(ANCHO))
        print("(╯‵□′)╯︵┻━┻".center(ANCHO))
        return
    else:
        ver_elementos(articulos)
        numero=input("Que orden quieres Eliminar: ".strip())
        while not numero.isdigit():
            print(f"{numero} no es una opcion valida. selecciona un numero de la lista.")
            ver_elementos(articulos)
            numero=input("intentalo orta vez: ".strip())
        
        numero=int(numero)
        if numero<1 or numero>len(articulos):
            print(f"no tenemos registro de la orden: {numero}")
        else:
            borrado=articulos.pop(numero-1)
            print(f"\nSe eliminó: x{borrado[2]}u. de {borrado[0]} {borrado[1]}")
            # print(f"Cancelaste la orden N°{borrado}")


"""  -------------------------MENU--------------------------------------  """
while True:  # mientras la condicion sea verdadera(true) se muestra el menu
    # TITULO
    # print("\n" * 2)  # espacio arriba
    titulo = "CRUD - INVENTARIO DE ARTICULOS"
    print(MARGEN)
    print(titulo.center(ANCHO)) #centrado del titulo
    subrayado = ("-" * len(titulo)) #subrayado segun largo del titulo
    print(subrayado.center(ANCHO))  
    
    # OPCIONES DEL MENU
    print("1. Crear items".ljust(20) + " 2. Ver items".rjust(ANCHO - 20),end="\n")
    print("3. Buscar item".ljust(20) + " 4. Eliminar items".rjust(ANCHO - 20))
    print("5. Salir".ljust(20))
    print("\n" * 2)  # espacio arriba, devolver a arriba de titulo
    opcion = input("ELIGE OPCION: ").strip() #QUITAR ESPACIOS

    # match-case para opciones 1-5 
    match opcion:
        case "1":  
            print(f"{MARGEN}\n","AGREGAR".center(ANCHO))
            cargar_elementos(articulos)
        case "2":
            print(f"{MARGEN}\n","VER".center(ANCHO))
            ver_elementos(articulos)
        case "3":
            print("BUSCAR".center(ANCHO))
            buscar(articulos)
        case "4":
            print("ELIMINAR".center(ANCHO))
            borrar_elementos(articulos)
        case "5":
            print("(っ°Д°;)っ".center(ANCHO))
            break
        case _:
            print("opcion no valida".upper().center(ANCHO))

# -------------------------.--------------------------------------


"""
Devolución - Pre-entrega CRUD (Pablo Velásquez)

✔️ Aspectos logrados:
- El menú está bien estructurado, con una presentación clara y legible.
- Se emplean funciones para organizar el código, separando correctamente la lógica de cada operación (crear, ver, eliminar).
- Buen uso de estructuras de control (while, match-case, enumerate) y mensajes al usuario que facilitan la interacción.
- Se manejan validaciones básicas en la carga de datos (nombre no vacío, stock mayor a cero).
- Se implementa una lista de listas como contenedor de registros, cumpliendo con la consigna mínima.
- El diseño visual (centrado, líneas, texto decorativo) le da una presentación cuidada al programa.

⚙️ Aspectos a mejorar / recomendaciones:
- La función buscar() está declarada pero no implementada: sería necesario completarla para cumplir el CRUD completo.
- La validación de eliminación tiene un error lógico en la línea if numero<1 or len(articulos)>numero: (debería ser if numero<1 or numero>len(articulos):).
- Podría agregarse control de errores al convertir stock_item a entero, para evitar que el programa se interrumpa si el usuario ingresa texto no numérico.
- En cargar_elementos(), algunas validaciones están duplicadas o confusas: el flujo podría simplificarse para no usar while anidados dentro de elif.
- Sería bueno agregar persistencia (CSV o SQLite) en futuras entregas para no perder los datos al cerrar el programa.
- Conviene mejorar la consistencia de los nombres de variables (por ejemplo, articulos y productos podrían uniformarse en futuras versiones).

💡 Sugerencias adicionales:
- Usar try/except para capturar errores de entrada y mantener el programa estable.
- Implementar mensajes de confirmación más claros (por ejemplo, “¿Desea eliminar este producto? s/n”).
- En una próxima etapa, se podría incorporar la actualización de datos (UPDATE) y almacenamiento permanente.

🌟 Observación final:
- El trabajo cumple con los requisitos mínimos de la pre-entrega, con una estructura funcional y legible. 
- Solo falta completar la función de búsqueda y ajustar detalles de validación. 
- Vas por muy buen camino, Pablo — tu presentación y manejo del menú muestran orden y comprensión del flujo lógico de un CRUD.

¡Excelente avance, seguí así! 

"""
# -------------------------.--------------------------------------
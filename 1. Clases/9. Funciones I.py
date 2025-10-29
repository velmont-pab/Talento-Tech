# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------
def saludar_usuario(user_name):
    """
    muestra un mensaje de bienvenida al usuario cuyo nombre se pasa como argumento a la función. 
    Parámetros:
    user_name (str): El nombre del usuario a saludar.
    Returns:
    None    
    """
    print(f"¡Hola! {user_name.capitalize()} Bienvenido/a al programa.")

name_user = input("como te llamas? ")

saludar_usuario(name_user)


# Parametros multiples
# argumentos posicionales

def describir_mascota(tipo,nombre):
    """
    describe una mascota con su tipo y nombre.

    Parámetros:
    tipo (str): representa el tipo de mascota.
    nombre (str): representa el nombre de la mascota.

    """
    print(f"tengo un {tipo} y se llama {nombre.capitalize()}")


# invocar la funcion

describir_mascota("perro","rocky")


# palabras clave como argumento
describir_mascota(nombre="luna",tipo="gato")


# valores por defecto
def describir_mascota2(nombre,tipo="perro"):
    """ describe una mascota con su tipo y nombre."""
    print(f"tengo un {tipo} y se llama {nombre.capitalize()}")

# default tipo es perro y se puede omitir 
describir_mascota2("max")

# si se quiere otro tipo, se puede especificar
describir_mascota2("nemo","pez")


def hacer_remera(talle,msj):
    """
    imprime los detalles de una remera con el talle y mensaje especificados.
    
    Parámetros:
    param1 (str): Talle de la remera
    param2 (str): mensaje impreso en la remera.
    
    Retorna:
    None
    """
    print(f"el talle de la remera es {talle.upper()} tiene un mensaje que dice  '{msj}' ")
    # talle = input("de que talle es tu remera? ")
    # msj = input("I love Python.")

hacer_remera("l","I love Python.")


while True:
    resp = input("quieres hacer una remera?\n(si/no): ").lower()
    if resp in ['si', 'no']:
        break
    print("Respuesta inválida, intenta de nuevo.")

""" 
    Agregar, modificar y eliminar elementos en listas y diccionarios es una operación común en la programación. 
    A continuación, te mostraré cómo hacerlo en Python, que es un lenguaje de programación muy popular y utilizado para este tipo de tareas.

    # Agregar elementos a una lista:
        Para agregar elementos a una lista en Python, puedes utilizar el método append() 
        # Método 1: usando append()
            mi_lista.append(4)
            print(mi_lista)  # Resultado: [1, 2, 3, 4]

        para agregar un elemento al final de la lista, o el método insert() 
        # Método 2: usando insert()
            mi_lista.insert(1, 5)  # Insertar el número 5 en la posición 1
            print(mi_lista)  # Resultado: [1, 5, 2, 3, 4]

        para agregar un elemento en una posición específica.
        # Agregar elementos a una lista
            mi_lista = [1, 2, 3]
            mi_lista.append(4)
            print(mi_lista)  # Resultado: [1, 2, 3, 4]

    # Modificar elementos en una lista:
        Para modificar elementos en una lista, simplemente accede al elemento mediante su índice y asigna un nuevo valor.
            mi_lista[0] = 10
            print(mi_lista)  # Resultado: [10, 5, 2, 3, 4]

    # Eliminar elementos de una lista
    Hay varias formas de eliminar elementos de una lista en Python: 
        como utilizar el método remove() para eliminar un valor específico. 
            # Eliminar por valor usando remove()
            mi_lista.remove(5)
            print(mi_lista)  # Resultado: [10, 2, 3, 4]

        el método pop() para eliminar por índice o la palabra clave del.
            # Eliminar por índice usando pop()
            mi_lista.pop(1)
            print(mi_lista)  # Resultado: [10, 3, 4]

    # Eliminar por índice usando del
        del mi_lista[1]
        print(mi_lista)  # Resultado: [10, 4]

    # Agregar y modificar elementos en un diccionario:
        En Python, los diccionarios tienen pares de clave-valor. 
        Puedes agregar nuevos pares clave-valor o modificar el valor asociado a una clave existente.

    # Crear un diccionario vacío
        mi_diccionario = {}

    # Agregar elementos al diccionario
        mi_diccionario['nombre'] = 'Juan'
        mi_diccionario['edad'] = 30
        print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 30}

    # Modificar el valor asociado a una clave existente
        mi_diccionario['edad'] = 31
        print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 31}

    # Eliminar elementos de un diccionario:
    Para eliminar un elemento de un diccionario, utiliza la palabra clave "del" y especifica la clave que deseas eliminar.

        del mi_diccionario['edad']
        print(mi_diccionario) 
        # Resultado: {'nombre': 'Juan'}

    Estos son los conceptos básicos para agregar, modificar y eliminar elementos en listas y diccionarios en Python. 
    Ten en cuenta que Python ofrece muchas más funciones y métodos para trabajar con estos tipos de datos, así que te animo a explorar más para aprovechar 
    todas las capacidades del lenguaje.




 """
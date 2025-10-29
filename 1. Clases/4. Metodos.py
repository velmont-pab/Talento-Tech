# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")






"""-------------------------LONGITUD DE CADENAS--------------------------------------

#len()
    La funcion es muy util para validar datos ingresados por el usuario.
    analizar cadenas o asegurarte de que cumplen con ciertos requisitos.
    como una cantidad minima o maxima de caracteres.
        INDICE INICIAL 
            El Primer caracter siempre esta en la posicion 0 
        INDICE FINAL
            El Ultimo caracter siempre esta en la posicion len(cadena)-1
        LONGITUD TOTAL
            Numero total de caracteres incluido espacios y simbolos
"""
cadena =input("Ingrese una cadena de texto: ")
longitud=len(cadena)
print(f"{cadena} contiene: {longitud} caracteres")

""" 
# MÉTODOS DE CADENAS (STRINGS)
    las cadenas en Python no solo son cadenas de caracteres, sino que tambien son objetos que vienen con una serie de metodos incorporados.
    Los metodos son funciones asociadas a las cadenas que podes utilizar para realizar operaciones comunes como cambiar el formato del texto, 
    buscar contenido o realizar transformaciones especificas.
        FUNCIONALIDAD
            operaciones predefinidas para manipular cadenas.
        INMUTABILIDAD
            Los metodos no modifican la cadena original,crean una nueva
        VERSATILIDAD
            amplia gama de operaciones para procesamiento de texto

-------------------------.lower()--------------------------------------
# FUNCION
    Convierte todos los caracteres de una cadena a minusculas.
    No modifica la cadena original
    Retorna una nueva cadena
    Mantiene numeros y simbolos sin cambios

# USO
    se usa frecuentemente en diversos escenarios de programacion.
    VALIDACION DE ENTRADA DE USUARIOS
    BUSQUEDAS INSENSIBLES A MAYUSCULAS
    NORMALIZACION DE DATOS
    COMPARACION DE DATOS
    PROCESAMIENTO DE CORREOS ELECTRONICOS
"""
# ejemplo 1:
texto="PyThOn"
print(texto.lower())
# ejemplo 2:
email=input("Ingrese su correo electronico: ")
if email.lower().endswith("@gmail.com"):
    print("Correo valido") 
else:
    print("Correo no valido")

"""-------------------------.upper()--------------------------------------
# FUNCION
    Convierte todos  los caracteres de la cadena a mayusculas.
    No modifica la cadena original
    Retorna una nueva cadena como resultado
    Mantiene intactos los numeros y simbolos especiales
# APLICACION
    sus usos mas comunes incluyen:
    Estandarizacion de titulos y encabezados
    formato de siglas y acronimos
    visualizacion de advertencias o mensajes importantes
    normalizacion de datos para comparaciones
 """
# ejemplo:
texto="PyThOn"
print(texto.upper())

"""-------------------------.strip()--------------------------------------
# FUNCION
    Elimina los espacios en blanco al principio y al final.
    Perfecto para limpiar entradas de usuario o datos importantes.
"""
# ejemplo:
texto="   Hola, Mundo!   "
print(texto.strip())
""" 
-------------------------.replace()--------------------------------------
# FUNCION
    reemplaza una subcadena por otra dentro de la cadena.
    muy util para realizar modificaciones de texto.
"""
# ejemplo:
texto="Hola, Mundo!"
print(texto.replace("Mundo","Python"))  
""" 
# -------------------------.startswith()--------------------------------------
# FUNCION
    devuelve TRUE si la cadena comienza con la subcadena especificada.
    De lo contrario devuelve FALSE. 
    Ideal para validaciones.
"""
# ejemplo:
texto="Hola, Mundo!"
print(texto.startswith("Hola"))

""" 
# -------------------------.endswith()--------------------------------------
# FUNCION
    devuelve TRUE si la cadena termina con la subcadena especificada.
    de lo contrario devuelve FALSE 
"""
# ejemplo:
texto="Hola, Mundo!"
print(texto.endswith("Mundo!"))

""" -------------------------.find()--------------------------------------
# FUNCION
    devuelve la posicion de la primera ocurrencia de una subcadena dentro de una cadena o -1 si no se encuentra. """
# ejemplo:  
texto="Hola, Mund!"
print(texto.find("Mundo"))
""" -------------------------.isdigit()--------------------------------------
# FUNCION
    Devuelve laposicion de la primera aparicion de una subcadena dentro de una cadena o -1 si no se encuentra. """
# ejemplo:
texto="12345"
print(texto.isdigit())

""" FORMAT STRING """
nombre = "Juan"
edad = 30
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))
print("Hola, mi nombre es %s y tengo %d años." % (nombre, edad))
print("Hola, mi nombre es {0} y tengo {1} años.".format(nombre, edad))
print("Hola, mi nombre es {nombre} y tengo {edad} años.".format(nombre=nombre, edad=edad))
print("Hola, mi nombre es {0} y tengo {1} años. {0} es un buen nombre.".format(nombre,edad))
print("Hola, mi nombre es {nombre} y tengo {edad} años. {nombre} es un buen nombre.".format(nombre=nombre, edad=edad))


""" 
¡Hola!
Estás haciendo un excelente trabajo. Luis me cuenta que estás explorando nuevas estructuras y comandos. Pero tengo trabajo para vos, ya que nuestro cliente nos pide que el programa que has desarrollado ahora haga lo siguiente:

1. Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera letra de cada palabra a mayúsculas y el resto en minúsculas.

2. Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.

3. Que clasifique a los y las clientes por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años.)
"""
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
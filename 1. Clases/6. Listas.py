# LIMPIAR TERMINAL
import os

os.system("cls" if os.name == "nt" else "clear")

"""---------------------------LISTAS----------------------------------------------------
# ES UNA ESTRUCTURA DE DATOS QUE PERMITE ALMACENAR MULTIPLES VALORES EN UN SOLO LUGAR
# Caracteristicas
    Pueden contener diferentes tipos de datos y son modificables.
# Sintaxis
    Se definen utilizando corchetes [] y los elementos se separan por comas.
# ejemplo:

lista_nums = [10, 20, 30, 40, 50]  # lista de numeros
print(lista_nums)

lista_cadena = ["ana", "luis", "carlos"]  # lista de cadena
print(lista_cadena)

lista_vacia = []  # lista vacia
print(lista_vacia)
"""

"""-------------------------FUNCIONES DE  LISTAS----------------------------------------------------
# ACCEDER A ELEMENTOS
# podemos acceder a los elementos de una lista utilizando su indice.
# el primer elemento tiene el indice 0, el segundo el indice 1 y asi sucesivamente. 
# ejemplo:
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # manzana
print(frutas[1])  # banana
print(frutas[2])  # cereza
print(frutas[1].insert(1,"frutilla")) # .insert(indice , elemento)

SI SE INTENTA ACCEDER A UN INDICE QUE NO EXISTE, SE GENERA UN ERROR DE TIPO IndexError.
print(frutas[3]) #IndexError: list index out of range
 
bicicletas = ["mountain", "bmx","paseo"]
print("▶",bicicletas[0].upper())  # Mountain

for bici in bicicletas:
    print("▶",bici.capitalize())
"""
"""
-------------------------AÑADIR ELEMENTOS----------------------------------------------------
motocicletas=[] # arrancamos con una lista vacia
# podemos añadir elementos a una lista utilizando el metodo append() o insert().
# append() añade el elemento al final de la lista.
# insert() añade el elemento en una posicion especifica. NO ELIMINA EL ELEMENTO ANTERIOR, SINO QUE LO CORRE TODA LA LISTA HACIA LA DERECHA. 
# ejemplo:

motocicletas.append("kawasaki")  # añadir "kawasaki" al final de la lista
print(motocicletas)
"""

"""
# -------------------------MODIFICAR ELEMENTOS----------------------------------------------------
# podemos modificar los elementos de una lista asignando un nuevo valor a un indice especifico.
# ejemplo:

motocicletas = ["honda", "yamaha", "suzuki"]
print(motocicletas)
motocicletas[1] = "ducati"  # cambiar "yamaha" por "ducati"
print(motocicletas[1])
""" 

"""
# -------------------------ELIMINAR ELEMENTOS----------------------------------------------------
podemos eliminar elementos de una lista utilizando el metodo 
    1. remove()  
        elimina la primera ocurrencia de un valor especifico.
        # ejemplo:
            motocicletas.remove("honda")  # eliminar "honda" de la lista
            print(motocicletas)
    2. pop()
        elimina un elemento en una posicion especifica y lo devuelve.
        # ejemplo:
            moto_eliminada = print(f"Se ha eliminado: {motocicletas.pop(-1)}")  # eliminar el ultimo elemento de la lista y guardarlo en una variable
            print(f"ultima moto: {moto_eliminada}")
            ultima_moto = motocicletas.pop(0)  # eliminar el primer elemento de la lista y guardarlo en una variable
            print(f"ultima moto: {ultima_moto}")
            print(motocicletas)
"""
""" 
# -------------------------LISTAS EN BUCLES WHILE---------------------------------------------------- 
indice = 0
while indice < len(lista_nums):
    print(f"El valor en el indice {indice} es: {lista_nums[indice]}")
    indice += 1
print("fin del bucle") 

# -------------------------LISTAS CON WHILE----------------------------------------------------
Para este ejercicio necesitamos un software que ayude a registrar y calcular información Para este ejercicio necesitamos un software que ayude a registrar y calcular información financiera básica para nuestros y nuestras clientes.

1. Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle while para solicitar el ingreso de cada mes. 
2. Validar que los ingresos sean números positivos. 
3. Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.
4. Calcular el total acumulado durante los 6 meses y el promedio mensual. Mostrá este resultado al final del programa.

ingresos = []
while len(ingresos) < 6:
    try:
        ingreso = float(input(f"Ingrese el ingreso del mes {len(ingresos) + 1}: "))
        if ingreso < 0:
            print("El valor no es válido. Por favor, ingrese un número positivo.")
        else: 
            ingresos.append(ingreso)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
total_acumulado = sum(ingresos)
promedio_mensual = total_acumulado / len(ingresos)
print(f"Total acumulado durante los 6 meses: {total_acumulado}")
print(f"Promedio mensual: {promedio_mensual}")

# -------------------------.--------------------------------------
CREAR LISTA DE INVITADOS ALMENOS 3 E IMPRIMIR 1 A 1  
    1. agrega 3 invitados mas pero 1 va a estar al inicio de la lista el 2do en el medio y el 3ro al final de la lista
    2. te avisan que no tenes mesa y solo pueden quedar 2 invitados, elimina hasta que queden 2
    3. imprime el mensaje de disculpas a los eliminados y el mensaje de confirmacion a los q quedan

invitados = []
reservacion = int(input("Cuantos invitados desea agregar a la lista (minimo 3): "))
while len(invitados) < reservacion :
    nombre = input("Ingrese el nombre del invitado: ").strip()
    if nombre:  # Verifica que el nombre no esté vacío
        invitados.append(nombre.capitalize())
    else:
        print("El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")

print(f"\nLista de invitados: {invitados}")




# -------------------------METODOS DE ORGANIZACION----------------------------------------------------
 
# sort() 
    ordena la lista en orden alfabetico o numerico.
        autos=["bmw","toyota","ford"]
        print(autos)
        autos.sort()    
        print(autos)

# reverse() 
    invierte el orden de la lista.
        autos.reverse()
        print(autos)    

#sorted() 
    devuelve una nueva lista ordenada sin modificar la original.
        print(sorted(autos))  # ['bmw', 'ford', 'toyota']
        print(autos)  # ['ford', 'toyota', 'bmw']


# -------------------------looping  DE LISTAS----------------------------------------------------
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta.title())
numeros= list(range(1,11)) # lista de numeros del 1 al 10
print(numeros)
numbers= list(range(2,21,2)) # lista de numeros impares del 1 al 20
print(numbers)


"""

# -------------------------.slices--------------------------------


jugadores = ["enzo","martina","ariel","gabriel","ale"]
print(jugadores[0:3])
print(jugadores[1:4])
print(jugadores[:4])
print(jugadores[2:])
print(jugadores[-3:])

for jugador in jugadores[:3]:
    print(jugador)



# print(jugadores[])
# print(jugadores[])
# print(jugadores[])
# print(jugadores[])
# print(jugadores[])
# print(jugadores[])





























# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
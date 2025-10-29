# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------

# -------------------------.--------------------------------------

# RETURN
    # las funciones pueden devolver valores usando la palabra reservada return 
    # cuando una función llega a una instrucción return, la función termina inmediatamente y devuelve el valor especificado.
    # Si no se especifica ningún valor después de return, la función devuelve None por defecto.
    # Una función puede tener múltiples instrucciones return, pero solo se ejecutará una de ellas, dependiendo de las condiciones dentro de la función.
    # El valor devuelto por una función puede ser asignado a una variable o utilizado directamente en expresiones.
    # Después de una instrucción return, cualquier código adicional dentro de la función no se ejecutará.
    # Las funciones pueden devolver múltiples valores utilizando tuplas.
    # Las funciones pueden devolver diferentes tipos de datos, como números, cadenas, listas, diccionarios, etc.
    # El uso de return permite que las funciones sean más flexibles y reutilizables, ya que pueden producir resultados que pueden ser utilizados en otras partes del programa.
    # Ejemplo:

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)

print(f"la suma es: {resultado}")   

# Ejemplo de multiple returns
def operaciones_matematicas(x, y):
    suma = x + y
    resta = x - y
    producto = x * y
    return suma, resta, producto

s, r, p = operaciones_matematicas(10, 5)
print(f"Suma: {s}, Resta: {r}, Producto: {p}") 

# Ejemplo de return temprano
def verificar_numero(num):
    if num < 0:
        return "Número negativo"
    return "Número positivo o cero"
print(verificar_numero(-3))
print(verificar_numero(4))
print(verificar_numero(0))

# Ejemplo de return sin valor
def funcion_sin_retorno():
    print("Esta función no devuelve nada.")
    return     
print(funcion_sin_retorno())  # Imprime None
# -------------------------.--------------------------------------  

# Ejemplo de return con diferentes tipos de datos
def obtener_datos():    
    nombre = "Ana"
    edad = 30
    intereses = ["lectura", "viajes", "música"]
    return nombre, edad, intereses  
n, e, i = obtener_datos()
print(f"Nombre: {n}, Edad: {e}, Intereses: {i}")    
# -------------------------.--------------------------------------
# Ejemplo de return con condicionales
def evaluar_nota(nota):
    if nota >= 7:
        return "Aprobado"
    else:
        return "Reprobado"
print(evaluar_nota(8))
print(evaluar_nota(5))
# -------------------------.--------------------------------------
def crear_persona(nombre,apellido):
    persona= {
        "nombre": nombre,
        "apellido": apellido
    }
    return persona

persona1 = crear_persona("juan","perez")
print(persona1)

for c,v in persona1.items():
    print(f"{c}: {v}")
# -------------------------.--------------------------------------

# docstrings y anotaciones de tipo 

def adicion(a, b):
    """
    Suma dos números y devuelve el resultado.
    Parámetros:
    a (int, float): El primer número a sumar.
    b (int, float): El segundo número a sumar.
    
    Returns:
    int, float: La suma de los dos números.
    """
    return a + b    
print(adicion(4, 5))
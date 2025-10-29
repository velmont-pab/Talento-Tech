# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------VARIABLES--------------------------------------
""" 
¿Qué es una Variable?
    En programación, una variable es como una "caja" donde podremos ingresar datos de distinto tipo y origen. 
    Es decir, se tratará de un contenedor en la memoria de tu computadora donde almacenaremos datos temporales que tu programa pueda usar y modificar mientras se ejecuta.
    1. Etiqueta Única
        Cada variable tiene un nombre único que permite acceder a su contenido.
    2. Almacenamiento Dinámico
        Las variables permiten que los programas sean flexibles y dinámicos. 
    3. Funcionamiento de Variables en Python
        En Python no necesitás declarar explícitamente el tipo de dato que una variable va a almacenar (como números, texto, listas, etc.). 
        Esto hace que trabajar con variables sea muy fácil.
        variable = valor
        mensaje = "Hola, Mundo"

En el contexto de la programación, el significado del signo “=” (operador de asignación) es diferente al significado que tiene en, 
por ejemplo, la matemática (igualdad).


# Formas de Asignación
    1. Asignación Única
        Se asigna un solo valor a una variable. Ejemplo: edad = 30
    2. Asignaciones Múltiples
        Se asignan valores a varias variables en una línea. Ejemplo: x, y, z = 1, 2, 3
    3. Cambio de Valor
        Se puede modificar el valor de una variable existente. Ejemplo: contador = contador + 1

# Nombres de Variables

    1. Caracteres Permitidos
        Letras, números y guiones bajos. Deben comenzar con letra o guion bajo.
    2. Palabras Reservadas
        No se pueden usar palabras reservadas de Python como nombres de variables.
    3. Sensibilidad a Mayúsculas
        Python distingue entre mayúsculas y minúsculas en nombres de variables.

# Buenas Prácticas en Nombres de Variables
    1. Descriptivos
        Usar nombres que reflejen claramente el contenido de la variable.
    2. Snake Case
        Usar minúsculas y guiones bajos para separar palabras en nombres largos.
    3.Evitar Nombres Cortos
        No usar nombres como "x" o "n" que no proporcionan información suficiente.


# Tipos de Datos Simples en Python
    Número Entero (int)
        Números sin parte decimal, positivos o negativos.
    Número Decimal (float)
        Números con parte fraccionaria separada por un punto.
    Cadena de Caracteres (str)
        Secuencias de caracteres para almacenar texto.
    Booleano (bool)
        Representa valores de verdadero (True) o falso (False).


# -------------------------TERMINAL--------------------------------------

# Función print()
    La función print() es utilizada para imprimir datos en la terminal.
    Acepta múltiples valores entre los paréntesis, los cuales pueden ser variables, literales (textos directos), o una combinación de ambos separados por comas

    Sintaxis:
        print(valor1, valor2)
    Ejemplo:
        nombre = "Mundo" print("Hola,", nombre) 
        “Hola” y nombre son dos argumentos.
    Salida por consola: 
        Hola, Mundo

# Caracteres Especiales en print()
    1. Nueva Línea (\n)
        Inserta un salto de línea en el texto impreso.
        print("Hola\nMundo")
        Salida por consola: 
            HolaMundo
    2. Tabulación (\t)
        Añade un conjunto fijo de espacios en blanco.
        print("Nombre:\tJuan\nEdad:\t30")
        Salida por consola:
            Nombre: Juan
            Edad: 30
    3. End
        Añade una especificación que se incorpora al final de la cadena
        print("Hola,", end=' ')
        print("Mundo")
        Salida por consola:
            Hola, Mundo

# Función input()
    Esta función permite a los programas utilizar datos introducidos por el la persona que usa el programa a través del teclado
    Funcionamiento
        Pausa la ejecución y espera que el usuario escriba algo.
        Devuelve lo escrito como una cadena de caracteres (string).
    Sintaxis:
        variable = input(prompt)
    Ejemplo:
        nombre = input("Introduce tu nombre: ")
        print("Hola", nombre)

# Función type()
    Esta función es una herramienta de desarrollo retorna el tipo de dato consultado.
    Sintaxis
        type(objeto)
    Uso
        Útil para verificar y depurar tipos de datos en el código.
    Ejemplos de Uso de type()
        print(type(10))        # <class 'int'>
        print(type(3.14))      # <class 'float'>
        print(type("Hola"))    # <class 'str'>
        print(type(True))      # <class 'bool'>

# -------------------------Conversión entre Tipos de Datos--------------------------------------

# Conversión entre Números Enteros y Decimales
    De int a float
        decimal = float(10) # Resultado: 10.0
    De float a int
        entero = int(3.14) # Resultado: 3

# Conversión de Números a Cadenas y Viceversa
    De int a str
        cadena = str(25)    # Resultado: "25"
    De str a int
        numero = int("123") # Resultado: 123

# Conversión entre Booleanos y Otros Tipos
    De bool a int
        True se convierte a 1, False a 0.
    De int a bool
        0 se convierte a False, cualquier otro número a True.

# Aplicación
    Útil en cálculos que dependen de condiciones lógicas.

    
    
# -------------------------Operadores Aritméticos--------------------------------------

Suma (+)
    Suma dos valores.
    resultado = 5 + 3 

Resta (-)
    Resta el segundo valor del primero.
    resultado = 5 - 3

Multiplicación (*)
    Multiplica dos valores.
    resultado = 5 * 3

División (/)
    Divide el primer valor entre el segundo.
    resultado = 6 / 3

Módulo (%)
    Devuelve el resto de la división.
    resultado = 7 % 3

Exponenciación (**)
    Eleva el primer valor a la potencia del segundo.
    resultado = 2 ** 3

División Entera (//)
    Divide y redondea hacia abajo al entero más cercano.
    resultado = 7 // 3


¡Hola!
En nuestro día a día, interactuamos con muchos clientes, y uno de los pasos iniciales es recopilar y organizar su información básica. 
Para eso, necesito que desarrolles un pequeño programa en Python que haga lo siguiente:
    Solicite al cliente su nombre, apellido, edad y correo electrónico.
    Almacene estos datos en variables.
    Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
¡Espero ver el resultado de tu trabajo pronto!
Saludos, Mariana”
"""
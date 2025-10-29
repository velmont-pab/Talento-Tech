# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------

#EJERCICIO 1
cadena =" Hola Mundo."

#INGRESO DE DATOS USANDO MATCH CASE
edad = int(input("Ingrese su edad: "))
match edad:
    case mayor if edad >= 18 :
        print("Eres mayor de edad ")
        print("la cadena secreta en mayusculas es: " ,cadena.upper())
        print("la cadena secreta en minusculas es: " ,cadena.lower())
        print("la cadena secreta tiene: " ,len(cadena), " caracteres")
        print("el ultimo caracter de la cadena secreta es: " ,cadena[-1])
    case menor if edad < 18 :
        print("Eres menor de edad ⚠ ")
        # for i in range(1,edad+1):
        #     print("Eres menor de edad ⚠ ",i)
        #     i+=1
    case _:
        print("Error, ingrese un valor valido")
# ----------------------------------------------------------------

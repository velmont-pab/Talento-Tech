# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")

# -------------------------BUCLES--------------------------------------

print("\n" * 2)  # espacio arriba
titulo = "NUMEROS PARES E IMPARES DEL 0 AL 100".center(60)
print(titulo)
consigna= print("es par".ljust(20).upper() + "ES IMPAR".rjust(40).lower())

# WHILE
n = 0
while n <= 100:
    if n % 2 == 0:
        print(f"{n}".ljust(20), end="") # evita que print() añada el salto de línea al final de lo que se imprime 🟡
    else:
        print(f"{n}".rjust(40))
    n+=1
print("\n" * 2)
# SENTENCIA BREAK+




# FOR RANGE



# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
# -------------------------.--------------------------------------
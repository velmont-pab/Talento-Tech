# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------

dimensiones=(200,40)

print(dimensiones[0])
print(dimensiones[1])


for i  in dimensiones:
    print(f"recorriendo una TUPLA: {i} y esta es su indice: ")


mi_lista = [
    ["pedro","meza","pmeza",],
    ["maria","sosa","msosa",],
]

y=enumerate(mi_lista)
print(y)

for j,i in enumerate(mi_lista):
    print(f"indice: {j+1}: {i}")
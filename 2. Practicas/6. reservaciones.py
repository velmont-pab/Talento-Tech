# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.---------------------

""" 
Crear una lista con los nombres de los y las clientes que vamos a procesar. 

1. Recorrer la lista y mostrar el nombre de cada cliente o clienta, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.). 

2. Si encuentras a alguien cuyo nombre sea una cadena en vacía, mostrar un mensaje de alerta indicando que ese dato no es válido. 

3. Para los nombres válidos, convertir cada uno a formato adecuado usando .capitalize(), de modo que siempre tengan la primera letra en mayúscula y el resto en minúscula. 

"""



# clientes = ["joey","monica","chandler","ross","rachel","phoebe",""]
# contador=0 
# largo_lista=len(clientes)

# while contador < largo_lista :
#     print(f"Cliente: {clientes[contador].capitalize()}".ljust(20), f"en la posicion: {contador+1}".strip())
#     if clientes[contador] =="": 
#         print(f"el nombre del cliente numero: {contador+1} no es valido")
#         nuevo_nombre = input("ingresa otro nombre: ").strip()
#         clientes[contador] = nuevo_nombre
#     contador += 1
# for index,nombre in enumerate(clientes):
#     print(f"Cliente: {nombre.capitalize()}".ljust(20), f"en la posicion: {index + 1}".strip())





# for h in range(0,len(clientes)): # imprime la lista con un formato
#     print(f"\tCliente: {clientes[h].capitalize()}".ljust(20),f"su posicion en la lista es: {h+1}".rjust(15))
#     if clientes[h] == "":
#         print(f"\nLo sentimos el nombre ingresado en {h+1} NO es valido.")
#         cambio = input("Ingresa un nombre: ").strip().capitalize()
#         clientes.remove(clientes[h])
#         clientes.append(cambio)

# for i in range(0,len(clientes)):
#     print(f"\tCliente: {clientes[i].capitalize()}".ljust(20), f"su posicion en la lista es: {i+1}".rjust(15).strip())

clientes = ["joey", "monica", "chandler", "ross", "rachel", "phoebe", ""]

# Anchos de columna
ancho_nombre = 20
ancho_posicion = 10

# Línea superior
print("+" + "=" * ancho_nombre + "+" + "=" * ancho_posicion + "+")

# Encabezados centrados
print("|" + "Cliente".center(ancho_nombre) + "|" + "Posición".center(ancho_posicion) + "|")

# Separador
print("+" + "-" * ancho_nombre + "+" + "-" * ancho_posicion + "+")

# Cuerpo de la tabla
for index, nombre in enumerate(clientes):
    nombre_formateado = nombre.capitalize() if nombre.strip() else "(Vacío)"
    posicion = str(index + 1)
    print("|" + nombre_formateado.center(ancho_nombre) + "|" + posicion.center(ancho_posicion) + "|")

# Línea inferior
print("+" + "=" * ancho_nombre + "+" + "=" * ancho_posicion + "+")

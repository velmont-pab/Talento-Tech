# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------


productos = [
    ("Manzana", 0.5, 20),
    ("Banana", 0.3, 35),
    ("Sandía", 1.25, 10),
    ("Durazno", 0.75, 50),
]

# Definir anchos de columnas
col1_width = 15  # Producto
col2_width = 10  # Precio
col3_width = 8  # Stock

# Crear separadores
horizontal_line = ("+" + "-" * col1_width + "+" + "-" * col2_width + "+" + "-" * col3_width + "+\n")

# Encabezado
header = ("|" + "Producto".center(col1_width) + "|" + "Precio".center(col2_width) + "|" + "Stock".center(col3_width) + "|\n")

# Construir el contenido de la tabla
tabla = horizontal_line + header + horizontal_line

for nombre, precio, stock in productos:
    fila = ( "|" + nombre.ljust(col1_width) + "|" + f"${precio:.2f}".rjust(col2_width) + "|" + str(stock).center(col3_width) + "|\n")
    tabla += fila

tabla += horizontal_line

# Guardar en archivo .txt
with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write(tabla)

print("✅ Archivo 'productos.txt' creado con éxito.")

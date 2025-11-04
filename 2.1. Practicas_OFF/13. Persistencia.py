import sqlite3  # Establecer la conexión a la base de datos 
from colorama import Fore, Style, init


# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------


init()
conexion = sqlite3.connect("productos.db") 
print(Fore.LIGHTGREEN_EX + "Conexión establecida exitosamente." + Style.RESET_ALL) 

 # Crear un objeto cursor 
cursor = conexion.cursor() 

# Crear una tabla 
cursor.execute(''' CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, precio REAL NOT NULL)''') 

print("Tabla 'productos' creada exitosamente.") 



print("Producto insertado exitosamente.")
# Confirmar los cambios y cerrar la conexión 
conexion.commit() 
# Cerrar la conexión 
conexion.close() 
# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------


estudiantes = {
    "Juan": {
        "edad": 20,
        "carrera": "Ingeniería",
        "promedio": 8.5,
        "materias": ["Matemáticas", "Física", "Programación"],
    },
    "Ana": {
        "edad": 22,
        "carrera": "Medicina",
        "promedio": 9.1,
        "materias": ["Anatomía", "Biología", "Química"],
    },
    "Luis": {
        "edad": 19,
        "carrera": "Derecho",
        "promedio": 7.8,
        "materias": ["Derecho Civil", "Derecho Penal", "Historia del Derecho"],
    },
    "María": {
        "edad": 21,
        "carrera": "Arquitectura",
        "promedio": 8.9,
        "materias": ["Diseño", "Geometría", "Historia del Arte"],
    },
    "Pedro": {
        "edad": 23,
        "carrera": "Economía",
        "promedio": 8.2,
        "materias": ["Microeconomía", "Macroeconomía", "Estadística"],
    },
    "Lucía": {
        "edad": 20,
        "carrera": "Psicología",
        "promedio": 9.4,
        "materias": ["Psicología General", "Neurociencia", "Estadística"],
    },
    "Carlos": {
        "edad": 18,
        "carrera": "Informática",
        "promedio": 8.7,
        "materias": ["Programación", "Redes", "Bases de Datos"],
    },
}
""" 
Diccionario que contiene información sobre varios estudiantes

 """

""" Tareas propuestas: """
# 1. Imprime nombres de estudiantes
for nombre in estudiantes.keys():
    print(f"Nombre del Estudiante: {nombre}, Inscripto en la carrera de {estudiantes[nombre]['carrera']}")

# 2. Mostrar solo los estudiantes con promedio mayor a 9.0
for nombre,nota in estudiantes.items():
    if nota["promedio"] >= 8.0:
        print(f"Estudiante: {nombre},",f"Promedio: {nota["promedio"]}".rjust(33,"_"))

# 3. Contar cuántos estudian cada carrera.
conteo_carreras = {}
""" 
lista vacia para almacenar las carreras a contar """
for k,v in estudiantes.items():
    carrera= v["carrera"] 
    if carrera in conteo_carreras:  # Verifica si la carrera ya está en el diccionario y suma 1
        conteo_carreras[carrera] += 1
    else:
        conteo_carreras[carrera] = 1    # Si no está, la agrega con valor 1
for carrera, cantidad in conteo_carreras.items():
    print(f"La carrera de {carrera} tiene {cantidad} estudiantes inscritos.")


# 4. Imprimir todas las materias de todos los estudiantes.
for k,v in estudiantes.items():
    materia = v["materias"]
    print(f"Las materias de {k.capitalize()} son:")
    # Recorremos cada materia para imprimirla una debajo de otra
    for materia in v["materias"]:
        print(f"\t- {materia}")


# 5. Agregar una nueva clave llamada `"año"` a cada estudiante.
for k,v in estudiantes.items():
    v["año"] = 1 # Asignamos el valor 1 a la nueva clave "año" para cada estudiante


# 6. Encontrar al estudiante con el mejor promedio.
mejor_estudiante = ""
mejor_promedio = 0.0
for k,v in estudiantes.items():
    if v["promedio"] > mejor_promedio:
        mejor_promedio = v["promedio"]
        mejor_estudiante = k
        print(f"Estudiante: {mejor_estudiante} promedio: {mejor_promedio}.")

# Respuesta de chatGpt 
# 7. Agregar un nuevo estudiante al diccionario.
nombre = input("Ingresar nombre del estudiante: ")
edad = int(input("Ingresar edad del estudiante: "))
carrera = input("Ingresar carrera: ")
promedio = float(input("Ingresar el promedio del estudiante: "))

# Agregar materias al estudiante
asignaturas = [] #crea lista vacia para almacenar las materias del nuevo estudiante
while True: #bucle infinito para ingresar materias
    asignatura = input("Ingresar materia/s (o 'salir' para terminar): ")
    if asignatura.lower() == "salir":
        break
    asignaturas.append(asignatura)

# ✅ Guardar todo, incluyendo las materias
estudiantes[nombre] = {
    "edad": edad,
    "carrera": carrera,
    "promedio": promedio,
    "materias": asignaturas,
}

# Mostrar las materias de todos los estudiantes
for k, v in estudiantes.items():
    print(f"\nLas materias de {k.capitalize()} son:")
    for materia in v["materias"]:
        print(f"\t- {materia}")


"""  mi error era que no agreba asignaturas a el nuevo estudiante

# 7. Agregar un nuevo estudiante al diccionario.
nombre = input("ingresar nombre del estudiante: ")
edad  = input("ingresar edad del estudiante: ")
carrera = input("ingresar carrera: ")
promedio = input("ingresar el promedio del estudiante: ")
estudiantes[nombre]={
    "edad":edad,
    "carrera":carrera,
    "promedio":promedio,}
# agregar materias al estudiante
asignaturas=[]
while True:
    asignatura=input("ingresar materia/s (o 'salir' para terminar): ")
    if asignatura .lower() == "salir":
        break
    asignaturas.append(asignatura)
# print(f"Las materias de {nombre} son: {asignaturas}")
for k, v in estudiantes.items():
    print(f"Las materias de {k} son:")
    # Recorremos cada materia para imprimirla una debajo de otra
    for materia in v["materias"]:
        print(f"\t- {materia}")
 """




"""
Vamos a desmenuzar este código paso a paso, explicando qué hace cada línea y por qué.

🧩 1️⃣ El diccionario base
    estudiantes = {
        "Juan": {"edad": 20, "carrera": "Ingeniería", "promedio": 8.5, "materias": ["Matemáticas", "Física", "Programación"]},
        "Ana": {"edad": 22, "carrera": "Medicina", "promedio": 9.1, "materias": ["Anatomía", "Biología", "Química"]},
        ...
    }


🔹 Aquí se crea un diccionario anidado llamado estudiantes.

    Cada clave principal (por ejemplo "Juan", "Ana", "Luis") es el nombre de un estudiante.

    El valor asociado a cada nombre es otro diccionario con los datos de esa persona (edad, carrera, promedio, materias).

👉 En resumen, tienes una estructura tipo:

    {
        "nombre_1":{"atributo": valor,"atributo": valor,...},
        "nombre_2":{"atributo": valor,"atributo": valor,...},
    }

🧩 2️⃣ Crear el diccionario vacío
    conteo_carreras = {}


🔹 Aquí se crea un diccionario vacío donde vamos a guardar el número de estudiantes por carrera.

Ejemplo esperado al final:
    {
    "Ingeniería": 1,
    "Medicina": 1,
    "Derecho": 1,
    ...
    }

🧩 3️⃣ Primer bucle for
    for nombre, datos in estudiantes.items():

🔍 ¿Qué hace esto?
    .items() devuelve pares (clave, valor) del diccionario estudiantes.
    
    En este caso:
    nombre → la clave principal (por ejemplo "Juan")
    datos → el diccionario interno con su información (por ejemplo {"edad": 20, "carrera": "Ingeniería", ...})

👉 Por lo tanto, este bucle va recorriendo cada estudiante y sus datos.

🧩 4️⃣ Acceder a la carrera del estudiante
    carrera = datos["carrera"]

🔹 Aquí accedemos al valor de la clave "carrera" dentro del diccionario datos.

    Ejemplo:
    Si datos = {"edad": 20, "carrera": "Ingeniería", ...}
    entonces carrera = "Ingeniería"

🧩 5️⃣ Condicional if
    if carrera in conteo_carreras:
        conteo_carreras[carrera] += 1
    else:
        conteo_carreras[carrera] = 1

🔍 Qué hace:

    Este bloque cuenta cuántos estudiantes hay por carrera:
    Si la carrera ya existe como clave en el diccionario conteo_carreras, significa que ya contamos al menos un estudiante de esa carrera.
👉 Entonces sumamos 1 al contador:
    conteo_carreras[carrera] += 1

    Si la carrera aún no existe (primer estudiante de esa carrera), la agregamos con valor 1:
    conteo_carreras[carrera] = 1


💡 Así, el diccionario se va llenando dinámicamente.

🧩 6️⃣ Segundo bucle for
    for carrera, cantidad in conteo_carreras.items():
        print(f"{carrera}: {cantidad} estudiante(s)")

🔍 Qué hace:
    .items() aquí recorre las claves y valores del diccionario conteo_carreras.
    En cada iteración:
    carrera → el nombre de la carrera.
    cantidad → el número de estudiantes en esa carrera.

📤 Luego imprime el resultado en un formato legible, por ejemplo:

    Ingeniería: 1 estudiante(s)
    Medicina: 1 estudiante(s)
    Derecho: 1 estudiante(s)
    Arquitectura: 1 estudiante(s)
    Economía: 1 estudiante(s)
    Psicología: 1 estudiante(s)
    Informática: 1 estudiante(s)
 """

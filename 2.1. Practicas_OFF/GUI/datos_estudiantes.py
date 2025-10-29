# datos_estudiantes.py
import json
import os

RUTA_ARCHIVO = "estudiantes.json"


def cargar_estudiantes():
    if os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}


def guardar_estudiantes(estudiantes):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, indent=4, ensure_ascii=False)


def crear_estudiante(nombre, edad, carrera, promedio, materias):
    return {
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio,
        "materias": materias,
    }


def agregar_estudiante(estudiantes, nombre, estudiante):
    estudiantes[nombre] = estudiante


def eliminar_estudiante(estudiantes, nombre):
    if nombre in estudiantes:
        del estudiantes[nombre]
        return True
    return False

# main_gui.py

import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from datos_estudiantes import (
    cargar_estudiantes,
    guardar_estudiantes,
    crear_estudiante,
    agregar_estudiante,
    eliminar_estudiante,
)

# LIMPIAR TERMINAL
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------

# Cargar los datos iniciales
estudiantes = cargar_estudiantes()

# -----------------------------
# FUNCIONES DE LA INTERFAZ
# -----------------------------


def actualizar_lista():
    """Actualiza la lista visual de estudiantes."""
    lista_estudiantes.delete(0, tk.END)
    for nombre in estudiantes.keys():
        lista_estudiantes.insert(tk.END, nombre)


def mostrar_detalles(event):
    """Muestra los detalles del estudiante seleccionado."""
    seleccion = lista_estudiantes.curselection()
    if not seleccion:
        return
    nombre = lista_estudiantes.get(seleccion)
    datos = estudiantes[nombre]
    detalles.set(
        f"Edad: {datos['edad']}\n"
        f"Carrera: {datos['carrera']}\n"
        f"Promedio: {datos['promedio']}\n"
        f"Materias: \n{', '.join(datos['materias'])}")


def agregar():
    """Agrega un nuevo estudiante desde ventanas de entrada."""
    ventana.after(100, lambda: ventana.focus_force())
    nombre = simpledialog.askstring("Nuevo estudiante", "Nombre del estudiante:",parent=ventana)
    if not nombre:
        return
    if nombre in estudiantes:
        messagebox.showerror("Error", "Ese estudiante ya existe.",parent=ventana)
        return
    ventana.after(100, lambda: ventana.focus_force())
    edad = simpledialog.askinteger("Edad", f"Edad de {nombre}:",parent=ventana)
    # ventana.after(100, lambda: ventana.focus_force())
    carrera = simpledialog.askstring("Carrera", f"Carrera de {nombre}:",parent=ventana)
    # ventana.after(100, lambda: ventana.focus_force())
    promedio = simpledialog.askfloat("Promedio", f"Promedio de {nombre}:",parent=ventana)
    # ventana.after(100, lambda: ventana.focus_force())
    materias = simpledialog.askstring("Materias", f"Materias de {nombre} (separadas por comas):",parent=ventana)

    lista_materias = [m.strip() for m in materias.split(",")] if materias else []

    nuevo = crear_estudiante(nombre, edad, carrera, promedio, lista_materias)
    agregar_estudiante(estudiantes, nombre, nuevo)
    guardar_estudiantes(estudiantes)
    actualizar_lista()
    messagebox.showinfo("Éxito", f"✅ Estudiante {nombre} agregado correctamente.",parent=ventana)


def eliminar():
    """Elimina el estudiante seleccionado."""
    seleccion = lista_estudiantes.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione un estudiante para eliminar.",parent=ventana)
        return

    nombre = lista_estudiantes.get(seleccion)
    confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar a {nombre}?",parent=ventana)

    if confirmar:
        eliminar_estudiante(estudiantes, nombre)
        guardar_estudiantes(estudiantes)
        actualizar_lista()
        detalles.set("")
        messagebox.showinfo("Eliminado", f"🗑️ {nombre} eliminado correctamente.",parent=ventana)

# 🟢 NUEVA FUNCIÓN: editar estudiante
def editar():
    """Permite editar los datos del estudiante seleccionado."""
    seleccion = lista_estudiantes.curselection()
    if not seleccion:
        messagebox.showwarning("Atención", "Seleccione un estudiante para editar.",parent=ventana)
        return

    nombre = lista_estudiantes.get(seleccion)
    datos = estudiantes[nombre]

    # Mostrar datos actuales y pedir nuevos valores
    ventana.after(100, lambda: ventana.focus_force())
    nueva_edad = simpledialog.askinteger("Editar Edad", f"Edad actual: {datos['edad']}",parent=ventana)
    # ventana.after(100, lambda: ventana.focus_force())
    nueva_carrera = simpledialog.askstring("Editar Carrera", f"Carrera actual: {datos['carrera']}",parent=ventana)
    # ventana.after(100, lambda: ventana.focus_force())
    nuevo_promedio = simpledialog.askfloat("Editar Promedio", f"Promedio actual: {datos['promedio']}",parent=ventana)
    # ventana.after(100, lambda: ventana.focus_force())
    nuevas_materias = simpledialog.askstring("Editar Materias",f"Materias actuales: {', '.join(datos['materias'])}\nIngrese nuevas (separadas por comas):",parent=ventana)

    # Actualizar valores (manteniendo los anteriores si el usuario deja en blanco)
    datos["edad"] = nueva_edad if nueva_edad is not None else datos["edad"]
    datos["carrera"] = nueva_carrera if nueva_carrera else datos["carrera"]
    datos["promedio"] = (nuevo_promedio if nuevo_promedio is not None else datos["promedio"])
    if nuevas_materias:
        datos["materias"] = [m.strip() for m in nuevas_materias.split(",")]

    guardar_estudiantes(estudiantes)
    mostrar_detalles(None)
    messagebox.showinfo("Actualizado", f"📝 Datos de {nombre} actualizados correctamente.",parent=ventana)


def salir():
    """Cierra la app."""
    guardar_estudiantes(estudiantes)
    ventana.destroy()
""" 

# -----------------------------
# INTERFAZ PRINCIPAL
# -----------------------------
ventana = tk.Tk()
ventana.title("📚 Sistema de Estudiantes")
ventana.geometry("700x400")
ventana.resizable(False, False)

# Lista de estudiantes
frame_lista = tk.Frame(ventana)
frame_lista.pack(side="left", fill="y", padx=10, pady=10)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista_estudiantes = tk.Listbox(
    frame_lista, yscrollcommand=scroll.set, width=25, height=20
)
lista_estudiantes.pack(side="left", fill="y")
scroll.config(command=lista_estudiantes.yview)
lista_estudiantes.bind("<<ListboxSelect>>", mostrar_detalles)

# Área de detalles
frame_detalles = tk.Frame(ventana)
frame_detalles.pack(side="left", expand=True, fill="both", padx=10, pady=10)

detalles = tk.StringVar()
label_detalles = tk.Label(frame_detalles,textvariable=detalles,justify="left",anchor="nw",font=("Arial", 12),)
label_detalles.pack(fill="both", expand=True)

# Botones inferiores
frame_botones = tk.Frame(ventana)
frame_botones.pack(side="bottom", fill="x", pady=5)

btn_agregar = tk.Button(frame_botones, text="➕ Agregar", width=12, command=agregar)
btn_agregar.pack(side="left", padx=10)

btn_editar = tk.Button(frame_botones, text="📝 Editar", width=12, command=editar)  # 🟢 nuevo botón
btn_editar.pack(side="left", padx=10)

btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", width=12, command=eliminar)
btn_eliminar.pack(side="left", padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", width=12, command=salir)
btn_salir.pack(side="right", padx=10)

# Cargar lista inicial
actualizar_lista()

# Iniciar app
ventana.mainloop()

 """


# -----------------------------
# INTERFAZ PRINCIPAL
# -----------------------------
ventana = tk.Tk()
ventana.title("📚 Sistema de Estudiantes")
ventana.geometry("700x400")
ventana.resizable(False, False)

# Frame contenedor para lista + detalles
frame_contenido = tk.Frame(ventana)
frame_contenido.pack(fill="both", expand=True)

# Lista de estudiantes
frame_lista = tk.Frame(frame_contenido)
frame_lista.pack(side="left", fill="y", padx=10, pady=10)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista_estudiantes = tk.Listbox(
    frame_lista, yscrollcommand=scroll.set, width=25, height=20
)
lista_estudiantes.pack(side="left", fill="y")
scroll.config(command=lista_estudiantes.yview)
lista_estudiantes.bind("<<ListboxSelect>>", mostrar_detalles)

# Área de detalles
frame_detalles = tk.Frame(frame_contenido)
frame_detalles.pack(side="left", expand=True, fill="both", padx=10, pady=10)

detalles = tk.StringVar()
label_detalles = tk.Label(
    frame_detalles,
    textvariable=detalles,
    justify="left",
    anchor="nw",
    font=("Arial", 12),
)
label_detalles.pack(fill="both", expand=True)

# Botones inferiores (separado del contenido)
frame_botones = tk.Frame(ventana)
frame_botones.pack(side="bottom", fill="x", pady=5)

btn_agregar = tk.Button(frame_botones, text="➕ Agregar", width=12, command=agregar)
btn_agregar.pack(side="left", padx=10)

btn_editar = tk.Button(frame_botones, text="📝 Editar", width=12, command=editar)
btn_editar.pack(side="left", padx=10)

btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", width=12, command=eliminar)
btn_eliminar.pack(side="left", padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", width=12, command=salir)
btn_salir.pack(side="right", padx=10)


# Cargar lista inicial
actualizar_lista()

# Iniciar app
ventana.mainloop()

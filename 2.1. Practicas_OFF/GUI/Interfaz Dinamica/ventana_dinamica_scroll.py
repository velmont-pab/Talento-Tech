"""
ventana_dinamica_scroll_fina.py
--------------------------------
Versión mejorada de la ventana dinámica con scroll en Tkinter.

✔ La barra de desplazamiento (scrollbar) se mantiene siempre a la derecha.
✔ El área de texto se adapta dinámicamente al tamaño de la ventana.
✔ Se utiliza un Canvas + Frame correctamente configurado para desplazamiento fluido.
✔ Incluye comentarios detallados y docstrings explicativos.
"""

import tkinter as tk
from tkinter import ttk


def crear_ventana():
    """Crea la ventana principal con área de texto dinámica y scroll correctamente alineado."""

    # ==============================
    # 1️⃣ Ventana principal
    # ==============================
    ventana = tk.Tk()
    ventana.title("Ventana dinámica con scroll alineado 🪟")
    ventana.geometry("800x500")
    ventana.minsize(400, 250)

    # Permite que la fila y columna 0 se expandan con la ventana
    ventana.rowconfigure(0, weight=1)
    ventana.columnconfigure(0, weight=1)

    # ==============================
    # 2️⃣ Frame principal (contenedor)
    # ==============================
    frame_principal = ttk.Frame(ventana)
    frame_principal.grid(row=0, column=0, sticky="nsew")

    # Permitir expansión en el frame
    frame_principal.rowconfigure(0, weight=1)
    frame_principal.columnconfigure(0, weight=1)

    # ==============================
    # 3️⃣ Canvas (área de scroll) + Scrollbar
    # ==============================
    canvas = tk.Canvas(frame_principal, highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Scrollbar vertical — siempre visible a la derecha del canvas
    scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Conectar scroll ↔ canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # ==============================
    # 4️⃣ Frame interior dentro del canvas (contenido real)
    # ==============================
    contenido_frame = ttk.Frame(canvas)
    contenido_window = canvas.create_window((0, 0), window=contenido_frame, anchor="nw")

    # ==============================
    # 5️⃣ Contenido dinámico dentro del frame
    # ==============================
    texto = (
        "🌟 Ejemplo de ventana dinámica con scroll siempre alineado a la derecha 🌟\n\n"
        "Este texto se ajusta automáticamente al ancho de la ventana, "
        "y la barra de desplazamiento acompaña el tamaño del contenido.\n\n"
        "🔹 Si haces la ventana más grande → el texto se expande.\n"
        "🔹 Si la achicas → aparece el scroll para desplazarte.\n\n"
        "Tkinter no tiene un contenedor 'scrollable' por defecto, "
        "pero combinando un Canvas con un Frame interno podemos lograrlo fácilmente.\n\n"
        "Este ejemplo usa 'grid' con pesos (weight) para que todo crezca de forma fluida.\n\n"
        "Prueba redimensionar la ventana y observa cómo la barra de desplazamiento "
        "permanece siempre visible a la derecha, mientras que el texto se adapta.\n\n"
        * 3)

    label_texto = tk.Label(
        contenido_frame,
        text=texto,
        justify="left",
        font=("Arial", 13),
        wraplength=700,  # se actualizará dinámicamente
        bg="#f5f5f5",
        padx=20,
        pady=20,
    )
    label_texto.pack(fill="both", expand=True)

    # ==============================
    # 6️⃣ Funciones dinámicas
    # ==============================

    def actualizar_scroll(event=None):
        """Ajusta el área visible del scroll al tamaño del contenido actual."""
        canvas.configure(scrollregion=canvas.bbox("all"))

    def ajustar_texto(event=None):
        """
        Ajusta automáticamente el ancho del texto (wraplength)
        al ancho actual de la ventana, menos un margen.
        """
        ancho_ventana = ventana.winfo_width()
        nuevo_wrap = max(300, ancho_ventana - 100)
        label_texto.config(wraplength=nuevo_wrap)

        # Ajustar el ancho del frame de contenido al canvas
        canvas.itemconfig(contenido_window, width=canvas.winfo_width())

        # Actualizar scroll
        actualizar_scroll()

    # Vincular eventos
    contenido_frame.bind("<Configure>", actualizar_scroll)
    ventana.bind("<Configure>", ajustar_texto)

    # ==============================
    # 7️⃣ Iniciar el bucle principal
    # ==============================
    ventana.mainloop()


# ==============================
# 🏁 Punto de entrada principal
# ==============================
if __name__ == "__main__":
    crear_ventana()

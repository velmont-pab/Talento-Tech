import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana dinámica con grid 🧩")
ventana.geometry("600x400")

# Configuramos filas y columnas para que se expandan
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=0)

# Frame principal que se ajusta
frame_texto = tk.Frame(ventana, bg="#e8e8e8")
frame_texto.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

texto = """Esta ventana usa 'grid' y se ajusta automáticamente.
El área de texto se expande con la ventana, mientras que los botones se mantienen abajo."""
label = tk.Label(
    frame_texto, text=texto, font=("Arial", 14), justify="left", wraplength=500
)
label.pack(fill="both", expand=True)

# Frame de botones
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=1, column=0, sticky="ew", pady=5)

btn1 = tk.Button(frame_botones, text="Aceptar", width=10)
btn2 = tk.Button(frame_botones, text="Cancelar", width=10)
btn1.pack(side="left", padx=10, pady=5)
btn2.pack(side="right", padx=10, pady=5)


# Ajustar el wraplength dinámicamente
def ajustar_texto(event):
    label.config(wraplength=ventana.winfo_width() - 60)


ventana.bind("<Configure>", ajustar_texto)
ventana.mainloop()

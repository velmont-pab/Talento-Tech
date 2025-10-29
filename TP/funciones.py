# LIMPIAR TERMINAL
import os
os.system("cls" if os.name == "nt" else "clear")
# -------------------------.--------------------------------------
def buscar(articulos):
    palabra = input("¿Qué estás buscando?\n").strip().lower()
    encontrados = []
    for art in articulos:
        if palabra in art[0] or palabra in art[1]:
            encontrados.append(art)

    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} coincidencia(s):")
        for art in encontrados:
            print(f"- {art[2]} de {art[1]}")
    else:
        print("No se encontró ningún producto con esa palabra.")

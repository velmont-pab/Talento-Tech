import os  # Para limpiar la pantalla con os.system
import keyboard  # Para detectar teclas presionadas
from colorama import Fore, Back, Style, init  # Para colores en consola

# Inicializa Colorama para que los colores se restablezcan automáticamente después de cada impresión
init(autoreset=True)


# --- Función que dibuja el menú en pantalla ---
def print_menu(options, selected_index):
    # Limpia la pantalla según el sistema operativo
    os.system("cls" if os.name == "nt" else "clear")

    # Título del menú en color cian y negrita
    print(Fore.CYAN + Style.BRIGHT + "=== MENÚ PRINCIPAL ===\n")

    # Itera sobre todas las opciones del menú
    for i, option in enumerate(options):
        if i == selected_index:
            # Si es la opción seleccionada, la resalta con fondo amarillo y texto negro
            print(Back.YELLOW + Fore.BLACK + f"> {option}" + Style.RESET_ALL)
        else:
            # Opciones no seleccionadas se imprimen normalmente
            print(f"  {option}")

    # Instrucciones al usuario
    print("\nUsa ↑ y ↓ para moverte, Enter para seleccionar. (ESC para salir)")


# --- Función principal ---
def main():
    # Lista de opciones del menú
    options = ["Iniciar juego", "Configuración", "Acerca de", "Salir"]
    selected = 0  # Índice de la opción actualmente seleccionada

    # Bucle infinito para mantener el menú activo hasta que el usuario salga
    while True:
        # Dibuja el menú con la opción seleccionada actual
        print_menu(options, selected)

        # Espera un evento de teclado (suppress=True evita que la tecla se muestre en consola)
        event = keyboard.read_event(suppress=True)

        # Solo actúa cuando se presiona la tecla (no al soltarla)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "up":  # Flecha arriba → mover selección hacia arriba
                selected = (selected - 1) % len(
                    options
                )  # Cicla al final si es necesario
            elif event.name == "down":  # Flecha abajo → mover selección hacia abajo
                selected = (selected + 1) % len(
                    options
                )  # Cicla al inicio si es necesario
            elif event.name == "enter":  # Enter → seleccionar opción
                os.system("cls" if os.name == "nt" else "clear")  # Limpiar pantalla
                print(
                    Fore.GREEN + f"Has seleccionado: {options[selected]}\n"
                )  # Mensaje de confirmación
                if (
                    options[selected] == "Salir"
                ):  # Si selecciona "Salir", termina el bucle
                    break
                input(
                    Fore.CYAN + "Presiona Enter para volver al menú..."
                )  # Pausa antes de volver al menú
            elif event.name == "esc":  # Escape → salir directamente
                break


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    main()

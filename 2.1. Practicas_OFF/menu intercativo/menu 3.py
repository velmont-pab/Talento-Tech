import os
import sys
import time
import keyboard
from colorama import Fore, Back, Style, init

# Inicializa Colorama
init(autoreset=True)


def print_menu(options, selected_index, cursor_visible=True):
    """
    Imprime el menú sobrescribiendo las líneas anteriores para un cursor parpadeante.
    """
    sys.stdout.write("\033[H")  # Mueve cursor a esquina superior izquierda
    sys.stdout.flush()

    print(Fore.CYAN + Style.BRIGHT + "=== MENÚ PRINCIPAL ===\n")

    for i, option in enumerate(options):
        if i == selected_index:
            cursor = ">" if cursor_visible else " "
            print(Back.YELLOW + Fore.BLACK + f"{cursor} {option}" + Style.RESET_ALL)
        else:
            print(f"  {option}")

    print("\nUsa ↑ y ↓ para moverte, Enter para seleccionar. (ESC para salir)")


def main():
    options = ["Iniciar juego", "Configuración", "Acerca de", "Salir"]
    selected = 0
    cursor_visible = True
    blink_interval = 0.1
    last_blink = time.time()

    # Limpiar pantalla al inicio
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\033[2J\033[H")

    while True:
        # Actualizar menú con cursor parpadeante
        print_menu(options, selected, cursor_visible)

        # Leer teclas sin bloquear
        if keyboard.is_pressed("up"):
            selected = (selected - 1) % len(options)
            while keyboard.is_pressed("up"):
                pass  # Espera a soltar la tecla para no saltarse opciones
        elif keyboard.is_pressed("down"):
            selected = (selected + 1) % len(options)
            while keyboard.is_pressed("down"):
                pass
        elif keyboard.is_pressed("enter"):
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.GREEN + f"Has seleccionado: {options[selected]}\n")
            if options[selected] == "Salir":
                break
            input(Fore.CYAN + "Presiona Enter para volver al menú...")
        elif keyboard.is_pressed("esc"):
            break

        # Actualizar parpadeo del cursor
        current_time = time.time()
        if current_time - last_blink >= blink_interval:
            cursor_visible = not cursor_visible
            last_blink = current_time

        # Pausa mínima para no saturar la CPU
        time.sleep(0.1)


if __name__ == "__main__":
    main()

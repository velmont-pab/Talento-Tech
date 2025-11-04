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
    cursor_visible: si True, muestra '>', si False se oculta
    """
    sys.stdout.write("\033[H")  # Mueve el cursor a la esquina superior izquierda
    sys.stdout.flush()

    # Título
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
    cursor_visible = True  # Controla el parpadeo

    # Limpiar pantalla al inicio
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.write("\033[2J\033[H")

    # Tiempo entre parpadeos
    blink_interval = 0.5

    last_blink = time.time()

    while True:
        # Actualizar menú solo si cambió el parpadeo o hubo movimiento
        print_menu(options, selected, cursor_visible)

        # Verificar si se presionó alguna tecla
        if keyboard.is_pressed("up"):
            selected = (selected - 1) % len(options)
            time.sleep(0.15)  # Pequeño delay para no saltarse opciones
        elif keyboard.is_pressed("down"):
            selected = (selected + 1) % len(options)
            time.sleep(0.15)
        elif keyboard.is_pressed("enter"):
            os.system("cls" if os.name == "nt" else "clear")
            print(Fore.GREEN + f"Has seleccionado: {options[selected]}\n")
            if options[selected] == "Salir":
                break
            input(Fore.CYAN + "Presiona Enter para volver al menú...")
        elif keyboard.is_pressed("esc"):
            break

        # Parpadeo del cursor
        current_time = time.time()
        if current_time - last_blink >= blink_interval:
            cursor_visible = not cursor_visible
            last_blink = current_time

        time.sleep(0.05)  # Pequeña pausa para no saturar CPU


if __name__ == "__main__":
    main()

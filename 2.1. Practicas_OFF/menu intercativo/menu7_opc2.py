import os
import sys
import time
from colorama import Fore, Back, Style, init
import shutil

# Inicializa Colorama
init(autoreset=True)


def print_menu(options):
    """
    Imprime el menú con opciones numeradas.
    """
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + Style.BRIGHT + "=== MENÚ PRINCIPAL ===\n")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print(
        "\nSelecciona una opción ingresando el número correspondiente (0 para salir)."
    )


def show_animated_banner(option_text, speed=0.02):
    """
    Muestra el título como un banner completo con efecto de deslizamiento.
    Ahora usa right_padding explícito para que sea más legible.
    """
    os.system("cls" if os.name == "nt" else "clear")
    terminal_width = shutil.get_terminal_size((80, 20)).columns

    # Texto con espacio a los lados
    banner_text = f" {option_text} "
    padding_total = max(terminal_width - len(banner_text), 0)
    left_padding = padding_total // 2
    right_padding = padding_total - left_padding

    # Construir banner vacío primero
    banner_line = " " * terminal_width
    sys.stdout.write(Back.YELLOW + Fore.BLACK + banner_line + Style.RESET_ALL + "\r")
    sys.stdout.flush()

    # Animar el texto deslizándose
    for i in range(len(banner_text)):
        # Calculamos los espacios a la derecha dinámicamente
        current_right_padding = right_padding + (len(banner_text) - (i + 1))
        line = " " * left_padding + banner_text[: i + 1] + " " * current_right_padding
        sys.stdout.write(Back.YELLOW + Fore.BLACK + line + Style.RESET_ALL + "\r")
        sys.stdout.flush()
        time.sleep(speed)

    print("\n")  # Salto de línea después del banner


def main():
    options = ["Iniciar juego", "Configuración", "Acerca de", "Salir"]

    while True:
        print_menu(options)

        choice = input(Fore.GREEN + "Tu elección: ")

        if not choice.isdigit():
            print(Fore.RED + "Por favor, ingresa un número válido.")
            input("Presiona Enter para continuar...")
            continue

        choice = int(choice)

        if choice == 0 or (
            1 <= choice <= len(options) and options[choice - 1] == "Salir"
        ):
            print(Fore.YELLOW + "¡Saliendo del programa!")
            break
        elif 1 <= choice <= len(options):
            show_animated_banner(options[choice - 1])
            input(Fore.CYAN + "Presiona Enter para volver al menú...")
        else:
            print(Fore.RED + "Número fuera de rango. Intenta de nuevo.")
            input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main()

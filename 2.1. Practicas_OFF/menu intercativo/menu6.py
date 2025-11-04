import os
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


def show_banner(option_text):
    """
    Muestra el título de la opción seleccionada como un banner completo con fondo de color.
    """
    os.system("cls" if os.name == "nt" else "clear")

    # Obtener el ancho de la terminal
    terminal_width = shutil.get_terminal_size((80, 20)).columns

    # Crear banner centrado
    text_length = len(option_text) + 2  # espacios a los lados
    if text_length < terminal_width:
        padding = (terminal_width - text_length) // 2
    else:
        padding = 0

    banner_line = (
        Back.YELLOW
        + Fore.BLACK
        + " " * padding
        + f" {option_text} "
        + " " * padding
        + Style.RESET_ALL
    )

    # Ajustar si el banner quedó corto por impar
    if len(banner_line) < terminal_width:
        banner_line += (
            Back.YELLOW + " " * (terminal_width - len(banner_line)) + Style.RESET_ALL
        )

    print(banner_line + "\n")


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
            show_banner(options[choice - 1])
            input(Fore.CYAN + "Presiona Enter para volver al menú...")
        else:
            print(Fore.RED + "Número fuera de rango. Intenta de nuevo.")
            input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main()

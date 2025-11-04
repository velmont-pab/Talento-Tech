import os
import sys
import time
from colorama import Fore, Back, Style, init

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


def show_animated_banner(option_text, speed=0.02, side_padding=4):
    """
    Muestra el título como un banner ajustado al tamaño del texto con borde y animación.
    speed: tiempo entre cada caracter (en segundos)
    side_padding: espacios a cada lado del texto
    """
    os.system("cls" if os.name == "nt" else "clear")

    # Preparar texto con padding
    padded_text = " " * side_padding + option_text + " " * side_padding
    banner_length = len(padded_text)

    # Construir líneas del banner con borde
    top_bottom = "+" + "-" * banner_length + "+"
    empty_line = "|" + " " * banner_length + "|"

    # Imprimir top del banner
    print(Back.YELLOW + Fore.BLACK + top_bottom + Style.RESET_ALL)

    # Animar línea del texto
    for i in range(1, len(padded_text) + 1):
        line = "|" + padded_text[:i] + " " * (banner_length - i) + "|"
        sys.stdout.write(Back.YELLOW + Fore.BLACK + line + Style.RESET_ALL + "\r")
        sys.stdout.flush()
        time.sleep(speed)

    print()  # Saltar línea después del texto
    # Imprimir bottom del banner
    print(Back.YELLOW + Fore.BLACK + top_bottom + Style.RESET_ALL + "\n")


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

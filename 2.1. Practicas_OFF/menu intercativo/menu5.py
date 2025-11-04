import os
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


def show_title(option_text):
    """
    Muestra el título de la opción seleccionada con fondo destacado.
    """
    os.system("cls" if os.name == "nt" else "clear")
    # Fondo naranja aproximado usando Back.YELLOW y texto negro
    print(
        Back.YELLOW
        + Fore.BLACK
        + Style.BRIGHT
        + f"  {option_text}  "
        + Style.RESET_ALL
        + "\n"
    )


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
            show_title(options[choice - 1])
            input(Fore.CYAN + "Presiona Enter para volver al menú...")
        else:
            print(Fore.RED + "Número fuera de rango. Intenta de nuevo.")
            input("Presiona Enter para continuar...")


if __name__ == "__main__":
    main()

""" 
Ejercicio: Validar datos de usuario
¡Hola!
Necesito que desarrolles un pequeño programa en Python que haga exactamente lo siguiente:
    1. Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.
    2. Compruebe que el nombre, el apellido y el correo NO estén en blanco, y que la edad sea MAYOR a 18 años.
    3. Muestre los datos por la terminal, en el orden que se ingresaron.
    4. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.

        Saludos, Mariana. """


nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = int(input("Por favor, ingresa tu edad: "))
correo = input("Por favor, ingresa tu correo electrónico: ")

if nombre == "" or apellido == "" or correo == "" or edad <= 18:
    print("ERROR!")
else:
    print("\n\t¡Bienvenido/a!\n")
    print("Tus datos son:")
    print(f"\tNombre: {nombre} \n\tApellido: {apellido}\n\tEdad: {edad}\n\tCorreo Electrónico: {correo}")

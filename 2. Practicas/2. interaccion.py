""" 
¡Hola!
En nuestro día a día, interactuamos con muchos clientes, y uno de los pasos iniciales es recopilar y organizar su información básica.
Para eso, necesito que desarrolles un pequeño programa en Python que haga lo siguiente:

1. Solicite al cliente su nombre, apellido, edad y correo electrónico.
2. Almacene estos datos en variables.
3. Los muestre organizados en forma de una tarjeta de presentación en la pantalla.

¡Espero ver el resultado de tu trabajo pronto!
Saludos, Mariana” """


nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
correo = input("Por favor, ingresa tu correo electrónico: ")

print("\n\t¡Hola Bienvenido!\n")
print("Tu tarjeta de presentación es:\n")
print(f"Nombre: {nombre} {apellido}\nEdad: {edad}\nCorreo Electrónico: {correo}")

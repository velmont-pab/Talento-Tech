

productos=[]

# funcion para validar que el texto no este vacio 
def pedir_dato(mensaje):
    while True:
        dato=input(mensaje).strip()
        if dato=="":
            print("ERROR!,dato invalido.")
        else:
            return dato
        
# funcion para crear un nuevo item
def crear_evento():
    print("crea item")
    nombre=pedir_dato("Ingrese el nombre del item: ")
    precio=pedir_dato("ingresa el precio: ")
    descripcion=pedir_dato("ingresa la descripcion del item: ")
    productos=[[nombre],[precio],[descripcion]]


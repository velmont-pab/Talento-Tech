"""
### Cómo aprender POO paso a paso

#### 1. **Conceptos básicos y vocabulario**

Antes de programar, asegúrate de entender bien estos conceptos:

* **Clase**: plantilla o molde para crear objetos.
* **Objeto (instancia)**: cada ejemplar creado a partir de una clase.
* **Atributos**: variables que describen características del objeto.
* **Métodos**: funciones que describen comportamientos de los objetos.
* **Encapsulamiento**: ocultar detalles internos (usando `_` o `__`).
* **Herencia**: una clase puede heredar atributos y métodos de otra.
* **Polimorfismo**: objetos de diferentes clases pueden ser tratados igual si tienen métodos similares.

---

#### 2. **Ejemplos simples**

Empieza escribiendo clases simples, creando objetos y accediendo a atributos/métodos.

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

mi_perro = Perro("Firulais")
mi_perro.ladrar()
```

---

#### 3. **Practica la creación de múltiples objetos**

Crea varias instancias para entender cómo cada objeto mantiene su estado.

---

#### 4. **Encapsulamiento simple**

Usa variables con `_` para simular atributos “privados” y crea métodos para acceder o modificar esos atributos (getters y setters).

---

#### 5. **Herencia**

Define una clase base y una clase hija que herede y amplíe funcionalidad.

```python
class Animal:
    def hablar(self):
        print("Animal hablando")

class Gato(Animal):
    def hablar(self):
        print("Miau")

g = Gato()
g.hablar()
```

---

#### 6. **Polimorfismo**

Crea funciones que reciban objetos de distintas clases y usen métodos con el mismo nombre.

---

#### 7. **Métodos y atributos especiales**

Familiarízate con `__init__`, `__str__`, `__repr__`, etc.

---

#### 8. **Ejercicios prácticos**

* Modela objetos de la vida real (coches, cuentas bancarias, empleados).
* Resuelve problemas donde la POO ayude a organizar el código.
* Lee código de proyectos simples que usen POO.

---

#### 9. **Recursos recomendados**

* Tutoriales de POO en Python (videos, blogs).
* Libros intro como *“Python Crash Course”* (tiene buen capítulo de POO).
* Cursos con ejercicios guiados.

---

### Tips para entender mejor POO

* **Piensa en objetos del mundo real**: una clase es como un molde para crear esos objetos.
* **Haz diagramas simples** para visualizar clases y relaciones.
* **No te preocupes por hacerlo perfecto al inicio**: práctica y repite.
* **Pregunta y juega con ejemplos** — prueba cambiar código y ver qué pasa.

---

Si quieres, puedo ayudarte con:

* Explicar un concepto con ejemplos simples.
* Crear ejercicios paso a paso.
* Revisar tu código y darte feedback.

¿Quieres que te prepare una mini guía práctica o un conjunto de ejercicios para empezar?
"""



""" 
    ¡Genial! Te voy a preparar una mini guía práctica con ejercicios paso a paso para que vayas entendiendo POO en Python de manera clara y práctica.

---

# Mini guía práctica para empezar con POO en Python

---

## Paso 1: Crear tu primera clase y objeto

**Ejercicio:**

Crea una clase `Animal` que tenga un atributo `nombre` y un método `hablar` que imprima `"El animal hace un sonido"`.

Luego, crea un objeto de esa clase con nombre `"Perro"` y llama al método `hablar`.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

# Crear objeto
animal = Animal("Perro")
animal.hablar()
```

---

## Paso 2: Modificar el método para usar el atributo

Cambia el método `hablar` para que imprima: `"El [nombre] hace un sonido"` usando el atributo `nombre`.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"El {self.nombre} hace un sonido")

animal = Animal("Perro")
animal.hablar()
```

---

## Paso 3: Crear una clase hija con herencia

Crea una clase `Perro` que herede de `Animal` y sobrescriba el método `hablar` para que imprima `"El [nombre] dice: Guau"`.

```python
class Perro(Animal):
    def hablar(self):
        print(f"El {self.nombre} dice: Guau")

perro = Perro("Firulais")
perro.hablar()
```

---

## Paso 4: Añadir atributos privados y métodos para acceder a ellos

Añade un atributo “privado” `__edad` a la clase `Perro` y crea métodos para obtener y cambiar la edad (getter y setter).

```python
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.__edad = edad

    def hablar(self):
        print(f"El {self.nombre} dice: Guau")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad inválida")

perro = Perro("Firulais", 3)
print(perro.get_edad())
perro.set_edad(5)
print(perro.get_edad())
```

---

## Paso 5: Crear método especial `__str__`

Agrega el método `__str__` para que al imprimir el objeto muestre algo amigable como: `"Perro: Firulais, 5 años"`.

```python
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.__edad = edad

    def hablar(self):
        print(f"El {self.nombre} dice: Guau")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("Edad inválida")

    def __str__(self):
        return f"Perro: {self.nombre}, {self.__edad} años"

perro = Perro("Firulais", 5)
print(perro)
```

---

## Paso 6: Ejercicio final para practicar

Crea una clase `CuentaBancaria` que tenga:

* Atributos: `titular` (nombre), `saldo` (inicializado en 0)
* Métodos:

  * `depositar(cantidad)` para añadir dinero
  * `retirar(cantidad)` para sacar dinero (solo si hay saldo suficiente)
  * `mostrar_saldo()` que imprima el saldo actual

Crea un objeto y prueba los métodos.

---

Si quieres, te puedo enviar las soluciones o ayudarte a resolver cada paso. También podemos agregar ejercicios más avanzados o específicos.

¿Quieres que te prepare la solución para el paso 6? ¿O prefieres que te guíe en alguno de los pasos anteriores?




 """
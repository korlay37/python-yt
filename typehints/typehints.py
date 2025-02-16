# 🔹 Hola, bienvenidos a otro video de Python.Hoy hablaremos de Type Hints, 
# una característica que nos ayuda a escribir código más claro y a evitar errores.
# Si bien Python es un lenguaje de tipado dinámico, lo que significa que no necesitamos declarar los tipos de variables.
# en 2014, con Python 3.5, se introdujeron los Type Hints como una forma de indicar los tipos esperados en el código.

# 🔹 ¿Qué es un Type Hint? Es una forma de indicar qué tipo de datos esperamos en las variables y funciones, sin cambiar el comportamiento de Python.
# Su único propósito es ayudar al editor de código y a las herramientas de análisis estático, como MyPy, a detectar errores antes de ejecutar el código.

# 📌 Explicación de Type Hints (1 - 2 min)
# 🔹 Normalmente, en Python no declaramos tipos de variables:

nombre = "Eduardo"
edad = 30


# Pero con Type Hints, podemos hacer esto más claro:
nombre: str = "Eduardo"
edad: int = 30

# 📌 Type Hints en funciones (2 - 3 min)
# 🔹 Ahora veamos cómo usar Type Hints en funciones:
def saludar(nombre: str) -> str:
    return f"Hola, {nombre}!"
# 🔹 Aquí estamos diciendo que nombre debe ser un str y que la función devuelve un str.

# 🔹 Otro ejemplo con números:
def sumar(a: int, b: int) -> int:
    return a + b
# 🔹 Esto ayuda a evitar errores al pasar valores incorrectos.

# 📌 Uso con listas y otros tipos (3 - 5 min)
# 🔹 También podemos usar Type Hints con listas y diccionarios:
numeros: list[int] = [1, 2, 3, 4]
edades: dict[str, int] = {"Ana": 25, "Luis": 30}

# 🔹 Así indicamos que numeros es una lista de enteros y edades es un diccionario con claves de tipo str y valores int.

# 🔹 ¡Y eso es todo! Ahora sabes qué son los Type Hints, cómo usarlos en variables y funciones, y cómo hacer tu código más claro.
# 🔹 No olvides suscribirte, dejar tu like y comentar si tienes dudas. Nos vemos en el próximo video! 🚀
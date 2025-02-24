# 🔥 5 Errores Comunes al Aprender Python (¡Evítalos desde Hoy!) 🚀

# Si estás aprendiendo Python, ¡evita estos 5 errores comunes que pueden frenar tu progreso! 🚀 En este video, te mostraré cuáles son y cómo solucionarlos con ejemplos prácticos.

# Desde el mal uso de variables hasta errores con listas y diccionarios, aquí aprenderás a escribir mejor código en Python. 🐍

# 🔹 ⏳ Marca de Tiempo:
# 00:00 Introducción
# 00:45 Error 1: No declarar bien las variables
# 02:10 Error 2: Problemas con listas mutables
# 03:45 Error 3: Errores con None y valores falsos
# 05:30 Error 4: No manejar excepciones correctamente
# 07:15 Error 5: Usar for cuando map() o list comprehension son mejores
# 09:00 Conclusión

# 📌 Sigue aprendiendo Python con más videos en el canal! 🎯

# ✅ "Hoy vamos a ver los 5 errores más comunes que comete la mayoría al aprender Python, y lo mejor de todo: te enseñaré cómo evitarlos con ejemplos prácticos. ¡Vamos a comenzar!"

# 🛑 1. No declarar bien las variables (0:45 - 2:10)
# 📌 Error: Usar nombres de variables poco descriptivos o sobrescribir funciones de Python.

# list = [18, 22, 19]  # ¡Mala práctica! "list" es una función en Python
# print(list)  
# Esto sobrescribe la función list(), causando errores en otras partes del código.
# edades: list[int] = [18, 22, 19]  # Usar nombres descriptivos
# print(edades)  

# 🛑 2. Problemas con listas mutables (2:10 - 3:45)
# 📌 Error: Modificar listas mutables sin darte cuenta cuando las pasas como argumento.

def agregar_elemento(lista: list[int]) -> None:
    lista.append(100)  # Modifica la lista original

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
print(mi_lista)  # ➝ [1, 2, 3, 100] ¡No era lo que esperabas!

# ✅ Solución:

def agregar_elemento2(lista: list[int]) -> list[int]:
    return lista + [100]  # Devuelve una nueva lista sin modificar la original

mi_lista = [1, 2, 3]
nueva_lista = agregar_elemento(mi_lista)
print(mi_lista)   # ➝ [1, 2, 3]
print(nueva_lista) # ➝ [1, 2, 3, 100]

# 🛑 3. Errores con None y valores falsos (3:45 - 5:30)
# 📌 Error: Comparar valores con None usando == en lugar de is.

valor = None
if valor == None:
    print("Es None")

# ✅ Solución:

if valor is None:
    print("Es None")

# 🛑 4. No manejar excepciones correctamente (5:30 - 7:15)
# 📌 Error: No manejar errores con try-except, lo que puede hacer que tu código se rompa.

numero:int = int(input("Ingresa un número: "))  # Si el usuario escribe "abc", el programa falla
print(10 / numero)

# ✅ Solución:

try:
    numero = int(input("Ingresa un número: "))
    print(10 / numero)
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")

# 📌 Siempre maneja excepciones para evitar que el programa se detenga inesperadamente.

# 🛑 5. Usar for cuando map() o list comprehensions son mejores (7:15 - 9:00)
# 📌 Error: Escribir código innecesariamente largo con for cuando hay formas más eficientes.

numeros = [1, 2, 3, 4]
dobles = []
for num in numeros:
    dobles.append(num * 2)

# ✅ Mejor solución con list comprehension:

dobles: list[int] = [num * 2 for num in numeros]
print(dobles)  # ➝ [2, 4, 6, 8]

# ✅ Otra opción con map():
dobles: list[int] = list(map(lambda x: x * 2, numeros))
print(dobles)  # ➝ [2, 4, 6, 8]


# 🎯 Conclusión (9:00 - 10:00)
# ✅ "Estos fueron los 5 errores más comunes al aprender Python y cómo evitarlos. Aprender a programar bien desde el principio te ahorrará tiempo y dolores de cabeza. Si este video te ayudó, no olvides suscribirte para más contenido sobre Python y desarrollo. 🚀 ¡Nos vemos en el siguiente video!"
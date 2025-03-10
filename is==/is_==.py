# 🚀 Si te gustó el video, dale like, comenta y suscríbete para más contenido de Python.
# 📚 ¿Quieres aprender Python desde cero? Mira mi curso en Udemy, el enlace está en la descripción.

# Hoy vamos a aclarar una duda común: ¿Cuál es la diferencia entre is y == en Python?
# 🔹 Aunque parecen similares, se usan para cosas diferentes y pueden causar errores si no los entiendes bien.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # ✅ True
print(a is b)  # ❌ False

# 📌 == compara valores, is compara identidad (1 - 3 min)
# ✅ == comprueba si los valores son iguales.
# ✅ is comprueba si dos variables apuntan al mismo objeto en memoria.
# 🔹 Ambas listas tienen los mismos elementos, pero son objetos distintos.

# 💡 Ejemplo con enteros pequeños:

x = 5
y = 5

print(x == y)  # ✅ True
print(x is y)  # ✅ True (Python optimiza enteros pequeños)
# 🔹 Python reutiliza ciertos valores pequeños (-5 a 256), por eso is da True aquí.

# 📌 ¿Cuándo usar is y ==? (3 - 5 min)
# ✅ Usa == cuando quieras comparar valores.
# ✅ Usa is cuando quieras verificar si dos variables apuntan al mismo objeto (ej. None).

# 💡 Ejemplo correcto con None:
valor = None

if valor is None:
    print("No hay valor definido")
# 🔹 Es una buena práctica usar is para verificar None en Python.
# En Python, None debe compararse con is en lugar de == porque None es un objeto singleton, 
# es decir, existe una única instancia de None en toda la ejecución del programa.


# 📌 Conclusión y cierre (5 - 6 min)
# ✅ == compara valores, is compara identidad en memoria.
# ✅ Para listas, diccionarios y objetos, is casi siempre será False.
# ✅ Usa is solo cuando realmente necesites verificar si es el mismo objeto.

# 🔹 ¿Te ha pasado algún error por confundir is y ==? Cuéntamelo en los comentarios.
# 🔹 Dale like y suscríbete para más tips de Python! 🚀
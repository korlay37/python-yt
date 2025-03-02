# 🔥 Qué son *args y **kwargs en Python y Cómo Usarlos (Ejemplos Fáciles!) 🐍

# 📌 Descripción Atractiva (+ Hashtags)
# 📌 ¿No entiendes *args y **kwargs en Python? Hoy te explico qué son, cómo usarlos y por qué son tan útiles. 🚀

# En este video, aprenderás:
# ✅ Cómo *args permite recibir múltiples argumentos posicionales.
# ✅ Cómo **kwargs maneja argumentos con nombre dinámicamente.
# ✅ Ejemplos prácticos y sencillos para entenderlo de una vez por todas.

# 💡 Después de este video, dominarás *args y **kwargs sin problemas!

# 🔹 ⏳ Marca de Tiempo:
# 00:00 Introducción
# 00:30 Qué es *args y cómo usarlo
# 02:30 Qué es **kwargs y cómo usarlo
# 04:30 Combinar *args y **kwargs en funciones
# 06:00 Conclusión

# 📌 Sigue aprendiendo Python con más videos en el canal! 🎯

# 🔽 Sígueme para más contenido sobre Python y desarrollo 🔽
# 🔥 Suscríbete ➝ [Tu enlace]
# 📢 Sígueme en Twitter ➝ [Tu enlace]
# 📩 Contacto ➝ [Tu correo]

# #Python #ArgsKwargs #Programación #PythonDesdeCero #DesarrolloWeb

# 🔹 Qué es *args y cómo usarlo
# 📌 *args permite pasar múltiples argumentos posicionales a una función.

def sumar(*args: int) -> int:
    return sum(args)

print(sumar(1, 2, 3, 4, 5))  # ➝ 15
print(sumar(10, 20))          # ➝ 30
# 📌 Explicación:
# ✔ *args convierte los argumentos en una tupla ((1, 2, 3, 4, 5)).
# ✔ sum(numeros) suma todos los valores automáticamente

# 🔹 Qué es **kwargs y cómo usarlo
# 📌 **kwargs permite recibir argumentos con nombre (clave-valor) en un diccionario.
def mostrar_info(**kwargs: str) -> None:
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Eduardo", lenguaje="Python", experiencia="Intermedio")
# 📌 Explicación:
# ✔ **kwargs convierte los argumentos en un diccionario ({'nombre': 'Eduardo', 'lenguaje': 'Python'}).
# ✔ .items() permite recorrer el diccionario dinámicamente.

# 🔹 Usar *args y **kwargs juntos
# 📌 Puedes combinar ambos para recibir cualquier tipo de argumento.
def procesar_datos(*args: int, **kwargs: str) -> None:
    print("Valores posicionales:", args)
    print("Valores con nombre:", kwargs)

procesar_datos(10, 20, 30, nombre="Ana", edad="25")
# 📌 Explicación:
# ✔ args recibe (10, 20, 30).
# ✔ kwargs almacena {'nombre': 'Ana', 'edad': '25'}.

# 🎯 Conclusión (06:00 - 06:30)
# ✅ "Ahora ya sabes cómo usar *argsy**kwargs en Python de manera efectiva. ¿Tienes dudas? Déjalas en los comentarios. ¡Suscríbete para más contenido sobre Python! 🚀"
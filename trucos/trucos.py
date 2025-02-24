# 🔥 3 Trucos de Python que Todo Principiante Debería Saber 🚀 (¡Ahorra Tiempo y Código!)

# 📌 ¿Quieres mejorar tu código en Python? Aquí te muestro 3 trucos esenciales que todo principiante debería conocer. 🐍

# 🔹 Cómo intercambiar variables sin una variable temporal.
# 🔹 Cómo usar enumerate() para hacer tus bucles más eficientes.
# 🔹 Cómo usar zip() para recorrer varias listas a la vez.

# ✅ ¡Aprende estos trucos y lleva tu código al siguiente nivel! 💡

# 🔹 ⏳ Marca de Tiempo:
# 00:00 Introducción
# 00:40 Truco 1: Intercambio de variables sin una variable extra
# 02:10 Truco 2: Usar enumerate() en lugar de range(len())
# 04:00 Truco 3: Recorrer múltiples listas con zip()
# 06:30 Conclusión

# 📌 Sigue aprendiendo Python con más videos en el canal! 🎯

# 🔽 Sígueme para más contenido sobre Python y desarrollo 🔽
# 🔥 Suscríbete ➝ [Tu enlace]
# 📢 Sígueme en Twitter ➝ [Tu enlace]
# 📩 Contacto ➝ [Tu correo]

#Python #TrucosPython #AprenderPython #DesarrolloWeb #Programación

# ✅ "Hoy te mostraré 3 trucos de Python que te ayudarán a escribir código más limpio, eficiente y profesional. ¡No te los pierdas!"

# 🛠️ Truco 1: Intercambiar variables sin una variable extra (00:40 - 02:10)
# 📌 Error común: Muchos principiantes intercambian valores con una variable temporal.

a: int = 5
b: int = 10

temp = a
a = b
b = temp

print(a, b)  # ➝ 10, 5

# ✅ Forma óptima con Python:

a, b = 5, 10
a, b = b, a  # Intercambio en una sola línea

print(a, b)  # ➝ 10, 5
# 🎯 ¿Por qué es mejor?

# Más rápido y más legible.
# No necesitas variables temporales.

# 🛠️ Truco 2: Usar enumerate() en lugar de range(len()) (02:10 - 04:00)
# 📌 Error común: Usar range(len(lista)) para iterar con índices.

# ❌ Código innecesariamente largo:
frutas: list[str] = ["manzana", "banana", "cereza"]

for i in range(len(frutas)):
    print(f"Índice {i}: {frutas[i]}")

# ✅ Forma más Pythonica con enumerate()
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")

# 🎯 Ventajas:
# ✔ Más legible y fácil de entender.
# ✔ Evita errores de IndexError.

# 🛠️ Truco 3: Recorrer múltiples listas con zip() (04:00 - 06:30)
# 📌 Error común: Usar múltiples for para recorrer listas en paralelo.

# ❌ Forma menos eficiente:
nombres: list[str] = ["Ana", "Luis", "Carlos"]
edades: list[int] = [25, 30, 22]

for i in range(len(nombres)):
    print(f"{nombres[i]} tiene {edades[i]} años")

# ✅ Forma más limpia con zip()
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
# 🎯 Ventajas:
# ✔ Código más corto y limpio.
# ✔ No necesitas manejar índices manualmente.

# 🎯 Conclusión (06:30 - 07:30)
# ✅ "Estos fueron 3 trucos esenciales de Python para escribir mejor código. ¿Cuál te sorprendió más? Déjalo en los comentarios. ¡No olvides suscribirte para más contenido sobre Python! 🚀"
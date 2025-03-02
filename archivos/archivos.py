# :
# 🔥 Cómo Leer y Escribir Archivos en Python en 5 Minutos (¡Súper Fácil!) 📝

# 📌 Aprende a leer y escribir archivos en Python de forma rápida y sencilla en solo 5 minutos. 🐍

# En este video, te mostraré:
# ✅ Cómo abrir archivos en modo lectura y escritura.
# ✅ Cómo leer archivos línea por línea o completamente.
# ✅ Cómo escribir y agregar contenido sin borrar el archivo.

# ¡Perfecto para principiantes y proyectos prácticos! 💡

# 🔹 ⏳ Marca de Tiempo:
# 00:00 Introducción
# 00:30 Leer un archivo de texto
# 02:00 Escribir en un archivo
# 03:30 Agregar contenido sin borrar el archivo
# 04:30 Conclusión

# 📌 Sigue aprendiendo Python con más videos en el canal! 🎯

# 🔽 Sígueme para más contenido sobre Python y desarrollo 🔽
# 🔥 Suscríbete ➝ [Tu enlace]
# 📢 Sígueme en Twitter ➝ [Tu enlace]
# 📩 Contacto ➝ [Tu correo]

# #Python #ArchivosPython #LeerArchivos #EscribirArchivos #DesarrolloWeb

# 📝 Leer un Archivo de Texto
def leer_archivo(nombre: str) -> str:
    with open(nombre, "r", encoding="utf-8") as archivo:
        contenido: str = archivo.read()
    return contenido

print(leer_archivo("ejemplo.txt"))
# 📌 Explicación:
# ✔ Se usa open(nombre, "r", encoding="utf-8") para abrir el archivo en modo lectura.
# ✔ .read() lee todo el contenido del archivo.
# ✔ El with open() cierra el archivo automáticamente.

# 📝 Leer un Archivo Línea por Línea
def leer_lineas(nombre: str) -> list[str]:
    with open(nombre, "r", encoding="utf-8") as archivo:
        lineas: list[str] = archivo.readlines()
    return lineas

print(leer_lineas("ejemplo.txt"))
# 📌 Explicación:
# ✔ .readlines() devuelve una lista con cada línea del archivo.
# ✔ Útil cuando necesitas procesar línea por línea.

# ✍️ Escribir en un Archivo (Sobreescribe el contenido
def escribir_archivo(nombre: str, contenido: str) -> None:
    with open(nombre, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)

escribir_archivo("ejemplo.txt", "¡Hola, Python!")
# 📌 Explicación:
# ✔ "w" (modo escritura) borra el contenido anterior y escribe el nuevo.
# ✔ .write() agrega texto al archivo.


# 📝 Agregar Texto sin Borrar el Contenido (Modo Append)
def agregar_archivo(nombre: str, contenido: str) -> None:
    with open(nombre, "a", encoding="utf-8") as archivo:
        archivo.write("\n" + contenido)

agregar_archivo("ejemplo.txt", "Nueva línea añadida.")
# 📌 Explicación:
# ✔ "a" (modo append) agrega contenido sin borrar lo anterior.
# ✔ "\n" asegura que el nuevo texto esté en una nueva línea.


# 🎯 Conclusión (04:30 - 05:00)
# ✅ "Ahora ya sabes cómo leer y escribir archivos en Python en menos de 5 minutos. ¿Te gustaría aprender más? Déjalo en los comentarios. ¡No olvides suscribirte para más contenido sobre Python! 🚀"


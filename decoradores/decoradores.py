# ¿Te gustaría modificar funciones sin cambiar su código? 
# Hoy te enseñaré cómo usar decoradores en Python de forma rápida y sencilla

# Un decorador es una función que recibe otra función como 
# argumento y la modifica antes de devolverla.
# Se usa para extender funcionalidades sin tocar el código original.

#  Ejemplos de uso común:
# ✔️ Medir tiempos de ejecución
# ✔️ Agregar logs automáticamente
# ✔️ Manejo de permisos

from typing import Callable

def mi_decorador(func: Callable) -> Callable:
    def wrapper() -> None:
        print("🔹 Antes de ejecutar la función")
        func()
        print("🔹 Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludo() -> None:
    print("👋 ¡Hola, mundo!")

saludo()

# 1️⃣ mi_decorador recibe una función y la envuelve con otra función interna.
# 2️⃣ La nueva función (wrapper) agrega código antes y después de ejecutar la original.
# 3️⃣ Con @mi_decorador, saludo() ahora tiene un comportamiento extra.

import time
from typing import Callable

def medir_tiempo(func: Callable[..., None]) -> Callable[..., None]:
    def wrapper(*args, **kwargs) -> None:
        inicio = time.time()
        func(*args, **kwargs)
        fin = time.time()
        print(f"⏳ Tiempo de ejecución: {fin - inicio:.4f} segundos")
    return wrapper

@medir_tiempo
def tarea() -> None:
    time.sleep(1)
    print("🎯 Tarea completada")

tarea()
#Python #Programación #POO #ClasesYObjetos #DesarrolloDeSoftware

# Curso de Python Profesional desde Cero: https://www.udemy.com/course/python-profesional-desde-cero-curso-basico/?couponCode=FEBRERO-2025

# 🔗 Web Personal: https://korlay37.vercel.app/
#  X : https://x.com/eduardo_rios_c
# ▶️ YouTube: https://www.youtube.com/@eduardo_rios
# 🖼️ Instagram: https://instagram.com/eduardorioscorlay
# 🎵 TikTok:  https://www.tiktok.com/@eduardo_rios_corlay
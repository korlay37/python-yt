# ¡Hola a todos! Bienvenidos a este video donde exploraremos formas útiles e interesantes de usar las F-strings en Python.
# Si crees que las F-strings son solo para mostrar variables, prepárate porque vamos a llevarlas al siguiente nivel. ¡Empecemos!"

# Las F-strings, son una forma poderosa de formatear cadenas. 
# Basta con anteponer una f al inicio de la cadena y usar llaves {} para insertar expresiones de Python."
a: int = 4
b: int = 3
print(f"numero 1: {a}, numero 2: {b}")

# Algo muy util que podemos hacer es usar las f strings combinadas con igual para ver resultados sin tener que escribir todo
print(f"a + b = {a + b}")
print(f"{a + b =}")


# Parte 2: Formateo numérico (2 minutos)
# Explica cómo las F-strings manejan el formateo de números con precisión, alineación y símbolos.
pi: float = 3.1415926535
print(f"{pi:.3f}")  # Resultado: 3.142

# Formatear numeros grandes
numero: int = 1234000
print(f"{numero:_}")
print(f"{numero:,}")

# combinar ambas opciones
num: float = 4432.2345
print(f"{num:,.2f}")

# formatear fechas
from datetime import datetime
now: datetime = datetime.now()
print(f"{now: %d--%m--%y ... %H:%H:%S}")
print(f"{now:%I%p}")

# Insertar espacios o caracteres
x: str = "Hola!"
print(f"Insertar izquiqerda: {x:10}")
print(f"Insertar derecha: {x:>10}")

# Centrar insertando espacios/caracteres
titulo: str = "Python Rocks"
print(f"{titulo:^20}")  # Centrado con asteriscos

valores: list[float] = [123.45, 67.89, 0.12]
for valor in valores:
    print(f"Valor alineado a la izquierda: {valor:10}")
    print(f"Valor alineado a la derecha: {valor:>10}")
    # print(f"Valor alineado a la derecha: {valor:>10.2f}")


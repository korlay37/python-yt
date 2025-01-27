# ¡Hola a todos! Hoy vamos a hablar de un tema esencial en Python y en muchos lenguajes de programación:
#  la Programación Orientada a Objetos o POO.
# En este video, exploraremos qué son las clases y los objetos, cómo crearlos y cómo usarlos en Python."


# La POO es un paradigma de programación que organiza el código en torno a objetos. 
# Un objeto es una representación de algo del mundo real, con propiedades (atributos) y acciones (métodos). 
# Por ejemplo, un coche tiene atributos como color y modelo, y métodos como arrancar o frenar."

class Coche:
    # "La función __init__ es el constructor de la clase. Se ejecuta cuando creamos un objeto y nos permite inicializar los atributos."
    def __init__(self, marca: str, modelo: str, color: str):
        # "Los atributos se almacenan usando self, que hace referencia al objeto que estamos creando."
        self.marca = marca  
        self.modelo = modelo
        self.color = color

    # "Los métodos, como arrancar y frenar, son funciones dentro de la clase que permiten que el objeto realice acciones."
    def arrancar(self) -> str:
        return f"El {self.marca} {self.modelo} está arrancando."

    def frenar(self) -> str:
        return f"El {self.marca} {self.modelo} está frenando."
    
    # Crear objetos a partir de la clase
mi_coche = Coche("Honda", "Civic", "gris")
otro_coche = Coche("Toyota", "Corolla", "rojo")

# Usar los métodos de los objetos
print(mi_coche.arrancar())  # Salida: El Toyota Corolla está arrancando.
print(otro_coche.frenar())  # Salida: El Honda Civic está frenando.
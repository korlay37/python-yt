mi_lista: list[str] = ["manzana", "pera", "cereza"]

# append(elemento)
# Agrega un elemento al final de la lista.
mi_lista.append("mandarina")
print(mi_lista)

# insert(posicion, elemento)
# Inserta un elemento en una posición específica.
mi_lista.insert(2, "sandia")
print(mi_lista)

# extend(iterable)
# Agrega todos los elementos de un iterable (como otra lista) al final de la lista.
mi_lista.extend(["platano", "melon"])
print(mi_lista)

# remove(elemento)
# Elimina la primera aparición de un elemento en la lista.
mi_lista.remove("pera")
print(mi_lista)

# pop(posicion)
# Elimina y devuelve el elemento en una posición específica. Si no se especifica, elimina el último
elemento: str = mi_lista.pop(2)
elemento: str = mi_lista.pop()

# sort(key=None, reverse=False)
# Ordena la lista en orden ascendente o descendente (en su lugar)
mi_lista.sort()
mi_lista.sort(key=lambda name: name.lower())
mi_lista.sort(key=lambda name: len(name))

# reverse()
# Invierte el orden de los elementos de la lista. (en su lugar)
mi_lista.reverse()

# count(elemento)
# Devuelve la cantidad de veces que un elemento aparece en la lista.
print(mi_lista.count("coco"))

# copy()
# Devuelve una copia superficial de la lista.
# Si la lista contiene elementos mutables, como sublistas o diccionarios, la copia mantiene referencias a esos objetos.
# Esto significa que si se modifica un elemento mutable dentro de la copia, el cambio se reflejará en la lista original
#  porque ambos apuntan al mismo objeto en memoria.
nueva_lista: list[str] = mi_lista.copy()

# index(elemento, inicio=0, fin=None)
# Devuelve el índice de la primera aparición del elemento. Opcionalmente, puedes buscar en un rango.
print(mi_lista.index("sandia"))

# clear
# Elimina todos los elementos de la lista, dejándola vacía.
mi_lista.clear()
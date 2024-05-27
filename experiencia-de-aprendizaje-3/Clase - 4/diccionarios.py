"""
Definición y Características:

Un diccionario es una colección de pares clave-valor.
Se define utilizando llaves {}.
Los elementos se almacenan en pares clave: valor.
Las claves deben ser únicas e inmutables (pueden ser números, cadenas, tuplas), mientras que los valores pueden ser de cualquier tipo.
Diferencias con Listas y Tuplas:

Las listas y tuplas son colecciones ordenadas; los diccionarios no tienen un orden específico.
Los elementos de listas y tuplas se acceden por índices; en diccionarios se acceden por claves.
"""
# Definición de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Imprimir el diccionario
print(mi_diccionario)


# Creación de un diccionario usando llaves
diccionario1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}

# Creación de un diccionario usando dict()
diccionario2 = dict(marca="Ford", modelo="Mustang", año=1964)

# Acceso a elementos
print(diccionario1["marca"])  # Imprime "Ford"
print(diccionario1.get("modelo"))  # Imprime "Mustang"

# Agregar o modificar elementos
mi_diccionario["color"] = "rojo"
mi_diccionario.update({"año": 2020})

"""Eliminar Elementos:

Usando el método pop().
Usando la palabra clave del.
Usando el método popitem() para eliminar el último par clave-valor.
Usando el método clear() para vaciar el diccionario."""
# Eliminar elementos
mi_diccionario.pop("edad")
del mi_diccionario["ciudad"]
mi_diccionario.popitem()  # Elimina el último par clave-valor
mi_diccionario.clear()  # Vacía el diccionario
"""

Memory updated
Clase Completa sobre Diccionarios en Python
Duración: 1 hora y 20 minutos

Objetivos de la Clase:
Definir qué es un diccionario en Python.
Explicar las diferencias entre diccionarios y otras estructuras de datos.
Mostrar cómo crear y manipular diccionarios.
Demostrar las principales funciones y métodos asociados con los diccionarios.
Proveer ejemplos prácticos de uso de diccionarios.
Proveer ejercicios prácticos para reforzar el aprendizaje.
Estructura de la Clase
1. Introducción a los Diccionarios (15 minutos)
Definición y Características:

Un diccionario es una colección de pares clave-valor.
Se define utilizando llaves {}.
Los elementos se almacenan en pares clave: valor.
Las claves deben ser únicas e inmutables (pueden ser números, cadenas, tuplas), mientras que los valores pueden ser de cualquier tipo.
Diferencias con Listas y Tuplas:

Las listas y tuplas son colecciones ordenadas; los diccionarios no tienen un orden específico.
Los elementos de listas y tuplas se acceden por índices; en diccionarios se acceden por claves.
Código de Ejemplo:

python
Copy code
# Definición de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Imprimir el diccionario
print(mi_diccionario)
2. Creación y Acceso a Elementos (10 minutos)
Creación de Diccionarios:

Usando llaves {}.
Usando el constructor dict().
Acceso a Elementos:

Usando la clave.
Usando el método get().
Código de Ejemplo:

python
Copy code
# Creación de un diccionario usando llaves
diccionario1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "año": 1964
}

# Creación de un diccionario usando dict()
diccionario2 = dict(marca="Ford", modelo="Mustang", año=1964)

# Acceso a elementos
print(diccionario1["marca"])  # Imprime "Ford"
print(diccionario1.get("modelo"))  # Imprime "Mustang"
3. Modificación de Diccionarios (10 minutos)
Agregar y Modificar Elementos:

Usando claves.
Usando el método update().
Eliminar Elementos:

Usando el método pop().
Usando la palabra clave del.
Usando el método popitem() para eliminar el último par clave-valor.
Usando el método clear() para vaciar el diccionario.
Código de Ejemplo:

python
Copy code
# Agregar o modificar elementos
mi_diccionario["color"] = "rojo"
mi_diccionario.update({"año": 2020})

# Eliminar elementos
mi_diccionario.pop("edad")
del mi_diccionario["ciudad"]
mi_diccionario.popitem()  # Elimina el último par clave-valor
mi_diccionario.clear()  # Vacía el diccionario
4. Funciones y Métodos Principales (20 minutos)
Funciones Built-in:

len(): Retorna el número de pares clave-valor.
str(): Retorna una representación en cadena del diccionario.
Métodos de Diccionarios:

keys(): Retorna una vista de todas las claves.
values(): Retorna una vista de todos los valores.
items(): Retorna una vista de todos los pares clave-valor.
copy(): Retorna una copia superficial del diccionario.
"""
# Definición de un diccionario
mi_diccionario = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Barcelona"
}

# Funciones built-in
print(len(mi_diccionario))  # Imprime 3
print(str(mi_diccionario))  # Imprime "{'nombre': 'Ana', 'edad': 30, 'ciudad': 'Barcelona'}"

# Métodos de diccionarios
print(mi_diccionario.keys())  # Imprime dict_keys(['nombre', 'edad', 'ciudad'])
print(mi_diccionario.values())  # Imprime dict_values(['Ana', 30, 'Barcelona'])
print(mi_diccionario.items())  # Imprime dict_items([('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Barcelona')])

# Crear una copia del diccionario
mi_diccionario_copia = mi_diccionario.copy()
print(mi_diccionario_copia)

# Definición de un diccionario
mi_diccionario = {
    "nombre": "Luis",
    "edad": 22,
    "ciudad": "Sevilla"
}

# Iterar sobre claves
for clave in mi_diccionario:
    print(clave)

# Iterar sobre valores
for valor in mi_diccionario.values():
    print(valor)

# Iterar sobre pares clave-valor
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")

"""
Las tuplas en Python o tuples son muy similares a las listas, pero con dos diferencias. Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.
"""
#Son una secuencia de elementos
mi_tupla = (1, 2, 3, "a", "b", "c")
# Imprimir la tupla
print(mi_tupla)

# Intentar modificar un elemento (esto causará un error)
# mi_tupla[0] = 100
"""Diferencias entre listas y tuplas:
    -listas son mutables las tuplas inmutables
    -
    
"""
# Diferentes formas de crear una tupla
tupla1 = (10, 20, 30)
tupla2 = 40, 50, 60
tupla3 = tuple([70, 80, 90])

# Acceso a elementos
print(tupla1[0])  # Imprime 10
print(tupla2[1:3])  # Imprime (50, 60)
# Definición de una tupla
mi_tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90)
# Obtener una sub-tupla desde el índice 2 hasta el 5 (sin incluir el índice 5)
sub_tupla1 = mi_tupla[2:5]
print(f"Sub-tupla desde el índice 2 hasta el 5 (sin incluir el 5): {sub_tupla1}")  # Imprime (30, 40, 50)
# Obtener una sub-tupla desde el inicio hasta el índice 3 (sin incluir el 3)
sub_tupla2 = mi_tupla[:3]
print(f"Sub-tupla desde el inicio hasta el índice 3 (sin incluir el 3): {sub_tupla2}")  # Imprime (10, 20, 30)
# Obtener una sub-tupla desde el índice 4 hasta el final
sub_tupla3 = mi_tupla[4:]
print(f"Sub-tupla desde el índice 4 hasta el final: {sub_tupla3}")  # Imprime (50, 60, 70, 80, 90)

# Obtener una sub-tupla con pasos (saltos), cada 2 elementos
sub_tupla4 = mi_tupla[1:8:2]
print(f"Sub-tupla con pasos (saltos) de 2 elementos desde el índice 1 hasta el 8: {sub_tupla4}")  # Imprime (20, 40, 60, 80)


# Intentar modificar la tupla
# tupla1[1] = 100  # Esto causará un error
# Definición de una tupla
tupla = (5, 10, 15, 20, 25, 5)

# Funciones built-in
print(len(tupla))  # Imprime 6
print(max(tupla))  # Imprime 25
print(min(tupla))  # Imprime 5
print(sum(tupla))  # Imprime 80

# Métodos de tuplas
print(tupla.count(5))  # Imprime 2
print(tupla.index(15))  # Imprime 2

# Desempaquetado de tuplas
tupla = (100, 200, 300)
a, b, c = tupla

print(a)  # Imprime 100
print(b)  # Imprime 200
print(c)  # Imprime 300

# Retornar múltiples valores desde una función
def coordenadas():
    return (10.0, 20.0)

x, y = coordenadas()
print(f"X: {x}, Y: {y}")  # Imprime X: 10.0, Y: 20.0

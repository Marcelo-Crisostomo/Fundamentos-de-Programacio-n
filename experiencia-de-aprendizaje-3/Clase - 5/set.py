
# Definición de un set
mi_set = {1, 2, 3, 4, 5}

# Imprimir el set
print(mi_set)
"""Creación de Sets:*9+6.0

Usando llaves {}.
Usando la función set()
Acceso a Elementos:

No se puede acceder a elementos por índice.
Se puede iterar sobre los elementos."""
# Creación de un set usando llaves
set1 = {10, 20, 30, 40, 50}

# Creación de un set usando set()
set2 = set([60, 70, 80, 90])

# Iterar sobre los elementos del set
for elemento in set1:
    print(elemento)

"""Agregar y Eliminar Elementos:

add(): Agrega un solo elemento.
update(): Agrega múltiples elementos.
remove(): Elimina un elemento específico (genera error si no existe).
discard(): Elimina un elemento específico (no genera error si no existe).
pop(): Elimina y retorna un elemento aleatorio.
clear(): Vacía el set."""
# Definición de un set
mi_set = {1, 2, 3}

# Agregar elementos
mi_set.add(4)
mi_set.update([5, 6, 7])

# Eliminar elementos
mi_set.remove(2)  # Genera error si el elemento no existe
mi_set.discard(3)  # No genera error si el elemento no existe

# Eliminar y retornar un elemento aleatorio
elemento = mi_set.pop()
print(f"Elemento eliminado: {elemento}")

# Vaciar el set
mi_set.clear()
print(mi_set)  # Imprime set()

"""Operaciones de Conjunto:

union(): Retorna la unión de dos sets.
intersection(): Retorna la intersección de dos sets.
difference(): Retorna la diferencia de dos sets.
symmetric_difference(): Retorna la diferencia simétrica de dos sets.
Operadores de Conjunto:

| para unión.
& para intersección.
- para diferencia.
^ para diferencia simétrica.
"""
# Definición de sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Operaciones de conjunto
union_set = set_a.union(set_b)
intersection_set = set_a.intersection(set_b)
difference_set = set_a.difference(set_b)
symmetric_difference_set = set_a.symmetric_difference(set_b)

print(f"Unión: {union_set}")
print(f"Intersección: {intersection_set}")
print(f"Diferencia: {difference_set}")
print(f"Diferencia Simétrica: {symmetric_difference_set}")

# Operadores de conjunto
union_set_op = set_a | set_b
intersection_set_op = set_a & set_b
difference_set_op = set_a - set_b
symmetric_difference_set_op = set_a ^ set_b

print(f"Unión (operador): {union_set_op}")
print(f"Intersección (operador): {intersection_set_op}")
print(f"Diferencia (operador): {difference_set_op}")
print(f"Diferencia Simétrica (operador): {symmetric_difference_set_op}")

"""Principales Métodos:

copy(): Retorna una copia superficial del set.
isdisjoint(): Retorna True si dos sets no tienen elementos en común.
issubset(): Retorna True si un set es subconjunto de otro.
issuperset(): Retorna True si un set es superconjunto de otro.
"""

# Definición de sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_c = {1, 2, 3, 4, 5}

# Copiar un set
set_copia = set_a.copy()
print(f"Copia: {set_copia}")

# Verificar si no tienen elementos en común
print(set_a.isdisjoint(set_b))  # False

# Verificar subconjunto
print(set_a.issubset(set_c))  # True

# Verificar superconjunto
print(set_c.issuperset(set_a))  # True

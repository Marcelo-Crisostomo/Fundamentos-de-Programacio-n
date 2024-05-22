"""
-Tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas.
-Podemos guardar en ellas lo que sea
- Mantienen el orden con el que fueron definidas.
- Pueden ser formadas por tipos arbitrarios
- Pueden ser indexadas con [i].
- Se pueden anidar, es decir, meter una dentro de la otra.
- Son mutables, ya que sus elementos pueden ser modificados.
- Son dinámicas, ya que se pueden añadir o eliminar elementos.
"""

# Definimos una lista con números del 1 al 10
lista = [1,2,3,4,5,6,7,8,9,10]

# Definimos una lista con elementos de diferentes tipos: un entero, una cadena y un flotante
a = [90, "Python", 3.87]
print(a[0]) # Imprime el primer elemento de la lista 'a', que es 90
print(a[1]) # Imprime el segundo elemento de la lista 'a', que es "Python"
print(a[2]) # Imprime el tercer elemento de la lista 'a', que es 3.87
# Se puede también acceder al último elemento usando el índice -1
print(a[-1]) # Imprime el último elemento de la lista 'a', que es 3.87
# Y si queremos modificar un elemento de la lista, basta con asignar con el operador = el nuevo valor.
a[2] = 1 # Cambia el tercer elemento de la lista 'a' a 1
print(a) # Imprime la lista modificada: [90, 'Python', 1]

# Un elemento puede ser eliminado con diferentes métodos, como veremos a continuación, o con del y la lista con el índice a eliminar.
l = [1, 2, 3, 4, 5]
del l[1] # Elimina el segundo elemento de la lista 'l'
print(l) # Imprime la lista modificada: [1, 3, 4, 5]

# También podemos tener listas anidadas, es decir, una lista dentro de otra.
x = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
print(x[3][0])    # Imprime el primer elemento de la cuarta sublista, que es 'p'
print(x[3][2][0]) # Imprime el primer elemento de la tercera sublista de la cuarta sublista, que es 5
print(x[3][2][2]) # Imprime el tercer elemento de la tercera sublista de la cuarta sublista, que es 7

# También es posible crear sublistas más pequeñas de una más grande usando el operador :
l = [1, 2, 3, 4, 5, 6]
l[0:3] = [0, 0, 0] # Cambia los tres primeros elementos de la lista 'l' a [0, 0, 0]
print(l) # Imprime la lista modificada: [0, 0, 0, 4, 5, 6]

# Se puede asignar una lista con n elementos a n variables.
l = [1, 2, 3]
x, y, z = l # Asigna 1 a x, 2 a y, y 3 a z
print(x, y, z) # Imprime los valores de x, y y z: 1 2 3

# Iterar listas
# En Python es muy fácil iterar una lista, mucho más que en otros lenguajes de programación.
lista = [5, 9, 10]
for l in lista:
    print(l)
# 5
# 9
# 10

# Si necesitamos un índice acompañado con la lista, que tome valores desde 0 hasta n-1, se puede hacer de la siguiente manera.
lista = [5, 9, 10]
for index, l in enumerate(lista):
    print(index, l)
# 0 5
# 1 9
# 2 10

# O si tenemos dos listas y las queremos iterar a la vez, también es posible hacerlo.
lista1 = [5, 9, 10]
lista2 = ["Jazz", "Rock", "Djent"]
for l1, l2 in zip(lista1, lista2):
    print(l1, l2)
# 5 Jazz
# 9 Rock
# 10 Djent

# Y por supuesto, también se pueden iterar las listas usando los índices y len()
lista1 = [5, 9, 10]
for i in range(0, len(lista1)):
    print(lista1[i])
# 5
# 9
# 10

# Métodos listas

# El método append() añade un elemento al final de la lista.
l = [1, 2]
l.append(3) # Añade el elemento 3 al final de la lista 'l'
print(l) # Imprime la lista modificada: [1, 2, 3]

# El método extend() permite añadir una lista a la lista inicial.
l = [1, 2]
l.extend([3, 4]) # Añade los elementos de [3, 4] al final de la lista 'l'
print(l) # Imprime la lista modificada: [1, 2, 3, 4]

# El método insert() añade un elemento en una posición o índice determinado.
l = [1, 3]
l.insert(1, 2) # Inserta el elemento 2 en la posición 1 de la lista 'l'
print(l) # Imprime la lista modificada: [1, 2, 3]

# El método remove() recibe como argumento un objeto y lo borra de la lista.
l = [1, 2, 3]
l.remove(3) # Elimina el elemento 3 de la lista 'l'
print(l) # Imprime la lista modificada: [1, 2]

# El método pop() elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite borrar elementos diferentes al último.
l = [1, 2, 3]
l.pop() # Elimina el último elemento de la lista 'l'
print(l) # Imprime la lista modificada: [1, 2]

# El método reverse() invierte el orden de la lista.
l = [1, 2, 3]
l.reverse() # Invierte el orden de la lista 'l'
print(l) # Imprime la lista invertida: [3, 2, 1]

# El método sort() ordena los elementos de menor a mayor por defecto.
l = [3, 1, 2]
l.sort() # Ordena la lista 'l' de menor a mayor
print(l) # Imprime la lista ordenada: [1, 2, 3]

# Y también permite ordenar de mayor a menor si se pasa como parámetro reverse=True.
l = [3, 1, 2]
l.sort(reverse=True) # Ordena la lista 'l' de mayor a menor
print(l) # Imprime la lista ordenada: [3, 2, 1]

# El método index() recibe como parámetro un objeto y devuelve el índice de su primera aparición.
l = ["Periphery", "Intervals", "Monuments"]
print(l.index("Intervals")) # Devuelve el índice de la primera aparición de "Intervals", que es 1

# También permite introducir un parámetro opcional que representa el índice desde el que comenzar la búsqueda del objeto.
l = [1, 1, 1, 1, 2, 1, 4, 5]
print(l.index(1, 4)) # Devuelve el índice de la primera aparición de 1 a partir del índice 4, que es 5
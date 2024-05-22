"""
OBJETIVOS DE LA CLASE
- Comprender qué es una matriz y cómo se utilizan en Python.
- Diferenciar entre matriz unidimensional, bidimensional y multidimensional.
- Aprender a crear y manipular matrices en Python.
- Prepararse para resolver la actividad práctica basada en estos conceptos.
"""
"""
Definición:
Una matriz es una estructura de datos que puede tener múltiples dimensiones. Puede ser vista como una colección de arreglos. Por ejemplo, una matriz bidimensional puede considerarse como una lista de listas en Python.
"""
#IMPORTANCIA DE LAS MATRICES EN LA PROGRAMACIÓN
#som apliamente utilizadas para manejar datos tabulares (tablas) y realizar operaciones matematicas (sumar o multiplicar 2 matrices iguales)

"""Matriz unidimensional:
    También conocida como vector, es una lista de elementos en una sola fila o columna.
"""
#Ejemplo de una matriz unidimensional.
matriz_1d = [1,2,3,4,5,60]
#acceder al primer elemento
primera_celda = matriz_1d[0]
print(f"primera celda: {primera_celda}")
#modificación de un elemento
matriz_1d[5]=6
print(matriz_1d)
"""#agregar elemento con el método append()
    El método append suele agregar un elemento al final de una lista, pero debemos saber manejarlo al agregar un elemento a una matriz bidimensional ya que al usar append se agregará una nueva fila al final.
    para especificar en estos casos debemeos utilizar
"""
matriz_1d.append(7)
print(matriz_1d)
#eliminar elementos con .remove()
matriz_1d.remove(7)
#ordenar matriz con .sort()
matriz_desordenada = [7,6,8,9,3,5,1,2,4,10]

matriz_desordenada.sort()
print(matriz_desordenada)

"""matriz Bidimensional
    Una matriz bidimensional es una lista de listas, es decir es una lista que cada otro elemento es otra lista.
    Su organización es filas(horizontal-x) y columnas(vertical-y)

"""
matriz_2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#Acceder al elemento, dibujar en la pizararra esta matriz----------
elemento_2d = matriz_2d[1][2]#Fila 2 columna 3
#modificar un elemento especifico
matriz_2d[2][2]= 10
# recorrer una matriz bidimensional con un ciclo for anidado
#Explicar con un dibujo como funciona el primer for recorriendo cada fila y el segundo for recorre cada elemento de esa fila y un vez finaliza, el primer ciclo for continúa con la siguiente fila y así sucesivamenete.
for fila in matriz_2d:
    for elemento in fila:
        print(elemento)
#end='' este parametro imprime por defecto un salto de lúnea.
"""Matriz Multidimensional:
    Una matriz multidimensional extiende el concepto de las matrices a más de dos dimensiones.
"""
matriz_3d = [
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
]
print(matriz_3d)
#Acceder a un elemento
elemento_3d = matriz_3d[1][0][2]
print(elemento_3d)
#modificar elementos
matriz_3d[1][0][2]=90
#recorrer una matriz tridimensional
print("="*10)
for dimension in matriz_3d:
    for fila in dimension:
        for elemento in fila:
            print (elemento)


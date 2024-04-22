#Comentario de una sola línea solo con # hash, gato o almoadilla
"""
Comentarios Multilinea en Python con comillas triples X3

Qúe es una variable en Python
Es un espacio de memoria reservado para almacenar datos que pueden cambiar durante la ejecución de un programa. 
Cada variable tiene un nombre único que la identifica y un valor asociado que puede ser de cualquier tipo de dato, como números, cadenas de texto, listas, diccionarios entre otros.

Python es un lenguaje de tipado dinámico no es necesario declarar explicitamente el tipo de una variable antes de usarla. 
El tipo de datos se infiere automáticamente según el valor asignado a la variable en tiempo de ejecución.
"""
#Nombres de Variables reglas:
#Pueden contener letras (mayúsculas o minúsculas), números y guiones bajos.
#Deben comenzar con una letra o un guion bajo.
variableCinco_5 = 5

#No pueden ser palabras reservadas de Python.
"""
Palabras reservadas en python: 
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif
else	except	finally	for	from	global	if, import, in, is, lambda, nonlocal, not, or
pass, raise, return, try, while	with y yield.

"""
#Case Sensitivity: Python distingue entre mayúsculas y minúsculas en los nombres de las variables. 
variableuno = 5
varibleUno = 6
# Tipos de datos en Python
# Números: enteros y de punto flotante
edad = 25  # Variable que almacena un número entero
altura = 1.75  # Variable que almacena un número de punto flotante
# Operaciones aritméticas con números
suma = 10 + 5 #Suma con +
resta = 20 - 8
multiplicacion = 4 * 6
division = 15 / 3

# Imprimir resultados de operaciones aritméticas
print("Suma:", suma)  # Imprime el resultado de la suma
print("Resta:", resta)  # Imprime el resultado de la resta
print("Multiplicación:", multiplicacion)  # Imprime el resultado de la multiplicación
print("División:", division)  # Imprime el resultado de la división

# Cadenas de texto se declaran entre comillas dobles o simples
nombreInstituto = "DUOC UC"  # Variable que almacena una cadena de texto
mensaje = '¡Hola, mundillo!'  # Otra variable que almacena una cadena de texto

# Concatenación de cadenas
saludo = "Hola, " + nombreInstituto + "!" # ,mensaje-- Concatena cadenas para formar un saludo personalizado
print(mensaje)  # Imprime el mensaje "¡Hola, mundillo!"
print(saludo)  # Imprime el saludo personalizado

# Booleanos
es_estudiante = True  # Variable que almacena un valor booleano
tiene_trabajo = True  # Otra variable que almacena un valor booleano

# Operaciones lógicas con booleanos
es_mayor_de_edad = edad >= 18  # Comprueba si la edad es mayor o igual a 18
puede_votar = es_mayor_de_edad and tiene_trabajo  # Comprueba si puede votar según su edad y situación laboral

# Imprimir resultados de operaciones lógicas
print("¿Es mayor de edad?", es_mayor_de_edad)  # Imprime si es mayor de edad
print("¿Puede votar?", puede_votar)  # Imprime si puede votar

#LISTAS: son colecciones ordenadas y modificables de elementos. Pueden contener elementos de diferentes tipos de datos y se definen utilizando corchetes [].
# Lista de números
numeros = [1, 2, 3, 4, 5]
# Lista de cadenas de texto
nombres = ["Juan", "María", "Pedro"]

# Lista mixta
mixta = [1, "Hola", True, 3.14]
# Acceder a elementos de una lista
print(numeros[0])  # Imprime el primer elemento de la lista de números
print(nombres[-1])  # Imprime el último elemento de la lista de nombres al poner - quiere decir ultimo -2 penultimo y así sucesivamente

#TUPLAS son colecciones ordenadas e inmutables de elementos. A diferencia de las listas, una vez creadas, no se pueden modificar. Se definen utilizando paréntesis ().
# Tupla de números
coordenadas = (10, 20)

# Tupla de cadenas de texto
meses = ("Enero", "Febrero", "Marzo")

# Acceder a elementos de una tupla
print(coordenadas[0])  # Imprime el primer elemento de la tupla de coordenadas
print(meses[-1])  # Imprime el último elemento de la tupla de meses

# CONJUNTOS: Los conjuntos son colecciones desordenadas y no indexadas de elementos únicos. Se definen utilizando llaves {} o la función set().
# Conjunto de números
numeros_primos = {2, 3, 5, 7, 11}
# Conjunto de letras
letras = set("Python3")
# Agregar elementos a un conjunto
numeros_primos.add(13)
# Eliminar elementos de un conjunto
letras.remove("3")
print(numeros_primos)
print(letras)

#DICCIONARIOS: Los diccionarios son colecciones desordenadas de pares clave-valor. Cada elemento se representa como una clave y su valor asociado. Se definen utilizando llaves {} y tienen la estructura clave: valor.
# Diccionario de persona
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Puerto Montt", "institucion":"DUOC UC"}
# Acceder a valores mediante claves
print(persona["nombre"])  # Imprime el nombre de la persona
print(persona["edad"])  # Imprime la edad de la persona
# Modificar valores de un diccionario
persona["edad"] = 35
# Agregar nuevos pares clave-valor
persona["profesion"] = "Ingeniero"
print(persona)
#CÓMO CAMBIAR EL VALOR DE UNA VARIABLE EN PYTHON Y EL TIPO DE DATO: simplemente asignándole un nuevo valor utilizando el operador de asignación =
# Definir una variable con un tipo de dato específico
valor = 10
# Imprimir el tipo de dato actual de la variable
print("Tipo de dato actual de la variable 'valor':", type(valor))
valor = 30
# Imprimir el tipo de dato  de la variable un cambiado
print("Tipo de dato actual de la variable 'valor':", type(valor))
# Cambiar el tipo de dato de la variable asignándole un nuevo valor de otro tipo
valor = "Hola"
# Imprimir el tipo de dato actualizado de la variable
print("Tipo de dato actualizado de la variable 'valor':", type(valor))

# Obtener un número entero del usuario
numero_str = input("Por favor, ingresa un número entero: ")

# Convertir el valor ingresado a un número entero
numero = int(numero_str)

# Realizar una operación matemática con el número ingresado
resultado = numero * 2

# Imprimir el resultado
print("El doble del número ingresado es:", resultado)
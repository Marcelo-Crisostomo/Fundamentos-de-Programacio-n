# Función que recibe una cantidad variable de argumentos (*args)
def suma_multiple(*args):
    """
    Esta función recibe una cantidad variable de números y devuelve su suma.
    """
    suma_total = 0
    for numero in args:
        suma_total += numero
    return suma_total

# Llamada a la función suma_multiple con varios argumentos
resultado_multiple = suma_multiple(1, 2, 3, 4, 5)
print(f"La suma de 1, 2, 3, 4 y 5 es {resultado_multiple}")

# Función que recibe una cantidad variable de argumentos con nombre (**kwargs)
def saludo_completo(**kwargs):
    """
    Esta función recibe una cantidad variable de argumentos con nombre y los usa para imprimir un saludo personalizado.
    """
    saludo = "Hola"
    for key, value in kwargs.items():
        saludo += f" {value}"
    saludo += ", bienvenidos a la clase de funciones en Python"
    print(saludo)

# Llamada a la función saludo_completo con argumentos con nombre
saludo_completo(nombre="Marcelo", apellido="González")

# Función combinada que usa *args y **kwargs
def informacion_completa(*args, **kwargs):
    """
    Esta función recibe una cantidad variable de argumentos y argumentos con nombre, y los imprime.
    """
    print("Información recibida:")
    for arg in args:
        print(f"Argumento: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Llamada a la función informacion_completa con varios tipos de argumentos
informacion_completa(1, 2, 3, nombre="Marcelo", curso="Fundamentos de Programación")

# Función que incluye procesamiento más complejo y devuelve varios valores
def estadisticas(*args):
    """
    Esta función recibe una cantidad variable de números y devuelve varias estadísticas: suma, promedio, máximo y mínimo.
    """
    suma_total = sum(args)
    promedio = suma_total / len(args)
    maximo = max(args)
    minimo = min(args)
    return suma_total, promedio, maximo, minimo

# Llamada a la función estadisticas con varios números
suma_total, promedio, maximo, minimo = estadisticas(10, 20, 30, 40, 50)
print(f"Suma: {suma_total}, Promedio: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")

# Función que recibe una lista y un diccionario y procesa ambos
def procesar_datos(lista, diccionario):
    """
    Esta función recibe una lista y un diccionario, y procesa ambos de distintas maneras.
    """
    print("Procesando lista:")
    for elemento in lista:
        print(f"Elemento: {elemento}")
    
    print("Procesando diccionario:")
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

# Llamada a la función procesar_datos con una lista y un diccionario
lista_ejemplo = [1, 2, 3, 4, 5]
diccionario_ejemplo = {"nombre": "Marcelo", "edad": 30}
procesar_datos(lista_ejemplo, diccionario_ejemplo)

# Ejemplo de una función recursiva para calcular el factorial de un número
def factorial(n):
    """
    Esta función calcula el factorial de un número de manera recursiva.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Llamada a la función factorial con el argumento 5
resultado_factorial = factorial(5)
print(f"El factorial de 5 es {resultado_factorial}")

# Función anidada: una función dentro de otra función
def operacion_anidada(a, b):
    """
    Esta función contiene otra función dentro de ella que realiza una operación matemática.
    """
    def suma(x, y):
        return x + y
    
    def multiplicacion(x, y):
        return x * y

    resultado_suma = suma(a, b)
    resultado_multiplicacion = multiplicacion(a, b)

    return resultado_suma, resultado_multiplicacion

# Llamada a la función operacion_anidada con argumentos 4 y 5
resultado_suma, resultado_multiplicacion = operacion_anidada(4, 5)
print(f"La suma de 4 y 5 es {resultado_suma} y la multiplicación es {resultado_multiplicacion}")

# Ejemplo de función lambda para elevar al cuadrado una lista de números
elevar_cuadrado = lambda x: x**2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Uso de la función map con la función lambda
numeros_cuadrados = list(map(elevar_cuadrado, numeros))
print(f"Los números {numeros} elevados al cuadrado son {numeros_cuadrados}")

# Ejemplo de uso de una función lambda en una función de orden superior
def aplicar_funcion(func, lista):
    """
    Esta función recibe otra función y una lista, y aplica la función a cada elemento de la lista.
    """
    return [func(elemento) for elemento in lista]

# Uso de la función aplicar_funcion con una función lambda para duplicar los números
duplicar = lambda x: x * 2
numeros_duplicados = aplicar_funcion(duplicar, numeros)
print(f"Los números {numeros} duplicados son {numeros_duplicados}")

# Función adicional 1: Uso de *args y **kwargs para operaciones matemáticas avanzadas
def operaciones_avanzadas(operacion, *args, **kwargs):
    """
    Esta función realiza operaciones matemáticas avanzadas basadas en el tipo de operación y los argumentos proporcionados.
    """
    resultado = 0
    if operacion == "suma":
        resultado = sum(args)
    elif operacion == "producto":
        resultado = 1
        for num in args:
            resultado *= num
    if kwargs.get('redondear'):
        resultado = round(resultado, kwargs['decimales'])
    return resultado

# Llamada a la función operaciones_avanzadas
resultado_suma_avanzada = operaciones_avanzadas("suma", 1, 2, 3, 4, 5, redondear=True, decimales=2)
print(f"Resultado de suma avanzada: {resultado_suma_avanzada}")

resultado_producto_avanzado = operaciones_avanzadas("producto", 1, 2, 3, 4, 5)
print(f"Resultado de producto avanzado: {resultado_producto_avanzado}")

# Función adicional 2: Aplicar múltiples funciones a una lista de valores
def aplicar_multiples_funciones(lista, *funcs):
    """
    Esta función aplica múltiples funciones a una lista de valores y devuelve los resultados.
    """
    resultados = []
    for func in funcs:
        resultados.append([func(elemento) for elemento in lista])
    return resultados

# Funciones lambda para aplicar
cuadrado = lambda x: x**2
cubo = lambda x: x**3

# Llamada a la función aplicar_multiples_funciones
resultados_multiples = aplicar_multiples_funciones(numeros, cuadrado, cubo)
print(f"Resultados aplicando cuadrado: {resultados_multiples[0]}")
print(f"Resultados aplicando cubo: {resultados_multiples[1]}")

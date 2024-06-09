# Ejemplo de función sin argumentos y sin retorno
def saludo():
    """
    Esta función imprime un saludo en pantalla.
    No toma argumentos y no retorna ningún valor.
    """
    print("Hola, soy una función sencilla.")
# Llamada a la función saludo
saludo()

# Ejemplo de función sin argumentos y con retorno
def obtener_suma():
    """
    Esta función suma dos números fijos y retorna el resultado.
    No toma argumentos y retorna la suma de los números.
    """
    num1 = 3
    num2 = 5
    return num1 + num2

# Llamada a la función obtener_suma e imprime el resultado
print("La suma es:", obtener_suma())

# Ejemplo de función con argumentos y sin retorno
def escribir_archivo(nombre_archivo, contenido):
    """
    Esta función toma dos argumentos: el nombre del archivo y
    el contenido a escribir. Escribe el contenido en el archivo
    especificado.
    """
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"Contenido escrito en {nombre_archivo}")

# Solicita el nombre del archivo y el contenido al usuario
nombre_archivo = input("Ingrese el nombre del archivo: ")
contenido = input("Ingrese el contenido a escribir en el archivo: ")

# Llama a la función escribir_archivo con los valores ingresados
escribir_archivo(nombre_archivo, contenido)

# Ejemplo de función con argumentos y con retorno
def leer_archivo(nombre_archivo):
    """
    Esta función toma el nombre de un archivo como argumento,
    lo lee y retorna su contenido.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "Error: Archivo no encontrado."

# Solicita el nombre del archivo al usuario
nombre_archivo = input("Ingrese el nombre del archivo a leer: ")

# Llama a la función leer_archivo y guarda el contenido
contenido_archivo = leer_archivo(nombre_archivo)

# Imprime el contenido del archivo
print(f"Contenido de {nombre_archivo}:\n{contenido_archivo}")

# Función con argumento y con retorno
def contar_palabras(contenido):
    """
    Esta función toma una cadena de texto como argumento y
    retorna el número de palabras en la cadena.
    """
    palabras = contenido.split()
    return len(palabras)

# Llama a la función contar_palabras y guarda el resultado
numero_palabras = contar_palabras(contenido_archivo)

# Imprime el número de palabras en el archivo
print(f"El archivo {nombre_archivo} tiene {numero_palabras} palabras.")

# Función para contar líneas en un archivo
def contar_lineas(contenido):
    """
    Esta función toma una cadena de texto como argumento y
    retorna el número de líneas en la cadena.
    """
    lineas = contenido.split('\n')
    return len(lineas)

# Llama a la función contar_lineas y guarda el resultado
numero_lineas = contar_lineas(contenido_archivo)

# Imprime el número de líneas en el archivo
print(f"El archivo {nombre_archivo} tiene {numero_lineas} líneas.")

# Función para contar caracteres en un archivo
def contar_caracteres(contenido):
    """
    Esta función toma una cadena de texto como argumento y
    retorna el número de caracteres en la cadena.
    """
    return len(contenido)

# Llama a la función contar_caracteres y guarda el resultado
numero_caracteres = contar_caracteres(contenido_archivo)

# Imprime el número de caracteres en el archivo
print(f"El archivo {nombre_archivo} tiene {numero_caracteres} caracteres.")

# Función para buscar una palabra en un archivo
def buscar_palabra(contenido, palabra):
    """
    Esta función toma una cadena de texto y una palabra como argumentos,
    y retorna el número de veces que la palabra aparece en la cadena.
    """
    return contenido.lower().split().count(palabra.lower())

# Solicita una palabra al usuario
palabra = input("Ingrese la palabra a buscar en el archivo: ")

# Llama a la función buscar_palabra y guarda el resultado
apariciones = buscar_palabra(contenido_archivo, palabra)

# Imprime el número de apariciones de la palabra en el archivo
print(f"La palabra '{palabra}' aparece {apariciones} veces en el archivo {nombre_archivo}.")

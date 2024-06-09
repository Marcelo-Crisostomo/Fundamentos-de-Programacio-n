# Función para escribir en un archivo
def escribir_archivo(nombre_archivo, contenido):
    """
    Esta función toma dos argumentos: el nombre del archivo y
    el contenido a escribir. Escribe el contenido en el archivo
    especificado.
    """
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print(f"Contenido escrito en {nombre_archivo}")
    except IOError:
        print("Error: No se pudo escribir en el archivo.")

# Función para leer un archivo
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

# Función para contar palabras en un contenido
def contar_palabras(contenido):
    """
    Esta función toma una cadena de texto como argumento y
    retorna el número de palabras en la cadena.
    """
    palabras = contenido.split()
    return len(palabras)

# Función para validar la entrada del usuario
def validar_entrada(mensaje):
    """
    Esta función toma una cadena como argumento que se utiliza
    para solicitar la entrada del usuario. Retorna la entrada
    validada.
    """
    while True:
        entrada = input(mensaje)
        if entrada.strip():
            return entrada
        else:
            print("Error: Entrada no válida. Intente nuevamente.")

# Solicita el nombre del archivo y el contenido al usuario con validación
nombre_archivo = validar_entrada("Ingrese el nombre del archivo para escribir: ")
contenido = validar_entrada("Ingrese el contenido a escribir en el archivo: ")

# Llama a la función escribir_archivo con los valores ingresados
escribir_archivo(nombre_archivo, contenido)

# Solicita el nombre del archivo al usuario para leer y validar la entrada
nombre_archivo = validar_entrada("Ingrese el nombre del archivo a leer: ")

# Llama a la función leer_archivo y guarda el contenido
contenido_archivo = leer_archivo(nombre_archivo)

# Verifica si el archivo fue leído correctamente
if "Error" not in contenido_archivo:
    # Llama a la función contar_palabras y guarda el resultado
    numero_palabras = contar_palabras(contenido_archivo)
    # Imprime el contenido del archivo y el número de palabras
    print(f"Contenido de {nombre_archivo}:\n{contenido_archivo}")
    print(f"El archivo {nombre_archivo} tiene {numero_palabras} palabras.")
else:
    # Imprime el mensaje de error si el archivo no fue encontrado
    print(contenido_archivo)

# Función adicional para contar líneas en un archivo
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

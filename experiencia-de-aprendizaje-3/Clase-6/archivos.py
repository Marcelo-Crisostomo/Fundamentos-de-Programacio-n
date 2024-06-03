# Importamos las librerías necesarias
import csv  # Para trabajar con archivos CSV
import json  # Para trabajar con archivos JSON

# Función para crear un archivo de texto (.txt)
def crear_archivo_txt(nombre_archivo, contenido):
    """
    Crea un archivo de texto y escribe contenido en él.
    :param nombre_archivo: nombre del archivo (string)
    :param contenido: contenido a escribir (string)
    """
    # Abre el archivo en modo escritura ('w') y crea uno nuevo si no existe
    with open(nombre_archivo, 'w') as archivo:
        # Escribe el contenido en el archivo
        archivo.write(contenido)
    # Imprime mensaje de confirmación
    print(f"Archivo {nombre_archivo} creado exitosamente.")

# Función para crear un archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    """
    Crea un archivo CSV y escribe datos en él.
    :param nombre_archivo: nombre del archivo (string)
    :param datos: lista de listas con los datos (list)
    """
    # Abre el archivo en modo escritura ('w') y crea uno nuevo si no existe
    with open(nombre_archivo, 'w', newline='') as archivo:
        # Crea un escritor CSV
        escritor_csv = csv.writer(archivo)
        # Escribe las filas en el archivo CSV
        escritor_csv.writerows(datos)
    # Imprime mensaje de confirmación
    print(f"Archivo {nombre_archivo} creado exitosamente.")

# Función para crear un archivo JSON
def crear_archivo_json(nombre_archivo, datos):
    """
    Crea un archivo JSON y escribe datos en él.
    :param nombre_archivo: nombre del archivo (string)
    :param datos: diccionario con los datos (dict)
    """
    # Abre el archivo en modo escritura ('w') y crea uno nuevo si no existe
    with open(nombre_archivo, 'w') as archivo:
        # Escribe el diccionario como JSON en el archivo
        json.dump(datos, archivo, indent=4)
    # Imprime mensaje de confirmación
    print(f"Archivo {nombre_archivo} creado exitosamente.")

# Ejemplo de uso de las funciones

# Crear un archivo de texto
contenido_txt = "Este es un archivo de texto de ejemplo."
crear_archivo_txt('ejemplo.txt', contenido_txt)

# Crear un archivo CSV
datos_csv = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', 25, 'Madrid'],
    ['Ana', 30, 'Barcelona'],
    ['Luis', 22, 'Valencia']
]
crear_archivo_csv('ejemplo.csv', datos_csv)

# Crear un archivo JSON
datos_json = {
    'nombre': 'Carlos',
    'edad': 28,
    'ciudad': 'Sevilla',
    'habilidades': ['Python', 'Django', 'Machine Learning']
}
crear_archivo_json('ejemplo.json', datos_json)

# Importamos las librerías necesarias
import csv  # Para trabajar con archivos CSV
import json  # Para trabajar con archivos JSON

# Función para crear un archivo de texto (.txt)
def crear_archivo_txt(nombre_archivo, contenido):
    """Crea un archivo de texto y escribe contenido en él."""
    # Abre el archivo en modo escritura ('w')
    # Si el archivo no existe, se crea uno nuevo
    with open(nombre_archivo, 'w') as archivo:
        # Escribe el contenido en el archivo
        archivo.write(contenido)
    # Imprime un mensaje de confirmación
    print(f"Archivo {nombre_archivo} creado exitosamente.")

# Función para crear un archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    """Crea un archivo CSV y escribe datos en él."""
    # Abre el archivo en modo escritura ('w')
    # El argumento newline='' se usa para evitar líneas en blanco adicionales en Windows
    with open(nombre_archivo, 'w', newline='') as archivo:
        # Crea un objeto escritor CSV
        escritor_csv = csv.writer(archivo)
        # Escribe las filas de datos en el archivo CSV
        escritor_csv.writerows(datos)
    # Imprime un mensaje de confirmación
    print(f"Archivo {nombre_archivo} creado exitosamente.")

# Función para crear un archivo JSON
def crear_archivo_json(nombre_archivo, datos):
    """Crea un archivo JSON y escribe datos en él."""
    # Abre el archivo en modo escritura ('w')
    with open(nombre_archivo, 'w') as archivo:
        # Convierte el diccionario de datos a formato JSON y lo escribe en el archivo
        json.dump(datos, archivo, indent=4)
    # Imprime un mensaje de confirmación
    print(f"Archivo {nombre_archivo} creado exitosamente.")

# Función para leer un archivo de texto (.txt)
def leer_archivo_txt(nombre_archivo):
    """Lee un archivo de texto y devuelve su contenido."""
    # Abre el archivo en modo lectura ('r')
    with open(nombre_archivo, 'r') as archivo:
        # Lee y devuelve todo el contenido del archivo
        return archivo.read()

# Función para leer un archivo CSV
def leer_archivo_csv(nombre_archivo):
    """Lee un archivo CSV y devuelve una lista de listas con los datos."""
    # Abre el archivo en modo lectura ('r')
    with open(nombre_archivo, 'r') as archivo:
        # Lee el contenido del archivo CSV y lo convierte en una lista de listas
        return list(csv.reader(archivo))

# Función para leer un archivo JSON
def leer_archivo_json(nombre_archivo):
    """Lee un archivo JSON y devuelve un diccionario con los datos."""
    # Abre el archivo en modo lectura ('r')
    with open(nombre_archivo, 'r') as archivo:
        # Lee el contenido del archivo y lo convierte de JSON a un diccionario
        return json.load(archivo)

# Función para agregar contenido a un archivo de texto existente
def agregar_contenido_txt(nombre_archivo, contenido):
    """Agrega contenido a un archivo de texto existente."""
    # Abre el archivo en modo agregar ('a')
    with open(nombre_archivo, 'a') as archivo:
        # Escribe el contenido adicional en el archivo
        archivo.write(contenido)
    # Imprime un mensaje de confirmación
    print(f"Contenido agregado al archivo {nombre_archivo} exitosamente.")

# Ejemplo de uso de las funciones de escritura y lectura
# Contenido para el archivo de texto
contenido_txt = "Este es un archivo de texto de ejemplo."
# Crear el archivo de texto con el contenido proporcionado
crear_archivo_txt('ejemplo.txt', contenido_txt)

# Datos para el archivo CSV
datos_csv = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', 25, 'Madrid'],
    ['Ana', 30, 'Barcelona'],
    ['Luis', 22, 'Valencia']
]
# Crear el archivo CSV con los datos proporcionados
crear_archivo_csv('ejemplo.csv', datos_csv)

# Datos para el archivo JSON
datos_json = {
    'nombre': 'Carlos',
    'edad': 28,
    'ciudad': 'Sevilla',
    'habilidades': ['Python', 'Django', 'Machine Learning']
}
# Crear el archivo JSON con los datos proporcionados
crear_archivo_json('ejemplo.json', datos_json)

# Leer y mostrar el contenido de los archivos
# Leer y mostrar el contenido del archivo de texto
print("Contenido del archivo de texto:")
print(leer_archivo_txt('ejemplo.txt'))

# Leer y mostrar el contenido del archivo CSV
print("\nContenido del archivo CSV:")
for fila in leer_archivo_csv('ejemplo.csv'):
    print(fila)

# Leer y mostrar el contenido del archivo JSON
print("\nContenido del archivo JSON:")
print(json.dumps(leer_archivo_json('ejemplo.json'), indent=4))

# Contenido adicional para el archivo de texto
contenido_adicional_txt = "\nEste es un contenido adicional."
# Agregar contenido al archivo de texto existente
agregar_contenido_txt('ejemplo.txt', contenido_adicional_txt)

# Leer y mostrar el contenido actualizado del archivo de texto
print("\nContenido actualizado del archivo de texto:")
print(leer_archivo_txt('ejemplo.txt'))

# Métodos adicionales para leer archivos
# Leer todo el contenido del archivo de una vez
with open('ejemplo.txt', 'r') as fichero:
    print("\nContenido leído con read():")
    print(fichero.read())

# Leer el archivo línea por línea usando readline()
with open('ejemplo.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != '':
        print(linea, end='')
        linea = fichero.readline()

# Leer el archivo línea por línea usando readlines()
with open('ejemplo.txt', 'r') as fichero:
    print("\nContenido leído con readlines():")
    for linea in fichero.readlines():
        print(linea, end='')

# Escribir en un archivo usando write() y writelines()
lista = ["Manzana\n", "Pera\n", "Plátano\n"]
# Abre el archivo en modo escritura ('w')
with open('datos_guardados.txt', 'w') as fichero:
    # Escribe la lista de elementos en el archivo
    fichero.writelines(lista)

# Ejemplo de comunicación entre dos funciones usando archivos
def escribe_fichero(mensaje):
    """Escribe un mensaje en un fichero."""
    # Abre el archivo en modo escritura ('w')
    with open('fichero_comunicacion.txt', 'w') as fichero:
        # Escribe el mensaje en el archivo
        fichero.write(mensaje)

def lee_fichero():
    """Lee un mensaje de un fichero y lo devuelve."""
    # Abre el archivo en modo lectura ('r')
    with open('fichero_comunicacion.txt', 'r') as fichero:
        # Lee el mensaje del archivo
        mensaje = fichero.read()
    # Borra el contenido del archivo abriéndolo en modo escritura ('w')
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write('')
    # Devuelve el mensaje leído
    return mensaje

# Usar las funciones de comunicación
# Escribe un mensaje en el archivo
escribe_fichero("Esto es un mensaje")
# Lee y muestra el mensaje del archivo
print("\nMensaje leído del fichero de comunicación:")
print(lee_fichero())

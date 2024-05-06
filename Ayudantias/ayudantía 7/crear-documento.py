import os

ruta_archivo = 'nuevo_documento.txt'
contenido = 'Este es el contenido del nuevo documento.\n¡Creado con Python!'

with open(ruta_archivo, 'w') as archivo:
    archivo.write(contenido)

print('Archivos en el directorio actual:')
print(os.listdir('.'))

with open(ruta_archivo, 'r') as archivo:
    contenido_leido = archivo.read()
    print(f'\nContenido del archivo:\n{contenido_leido}')
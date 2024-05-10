try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("El archivo no existe")
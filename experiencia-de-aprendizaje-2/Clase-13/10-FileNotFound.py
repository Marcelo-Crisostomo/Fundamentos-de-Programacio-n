try:
    file = open("archivo.txt", "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
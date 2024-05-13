try:
    file = open("archivo.txt", "r")
    content = file.read()
    file.close()
except IOError:
    print("Error: Error de entrada/salida.")
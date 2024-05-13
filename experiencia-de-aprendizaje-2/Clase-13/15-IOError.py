try:
    file = open("archivoss.txt", "r")
    content = file.read()
    file.close()
except IOError:
    print("Error: Error de entrada/salida.")
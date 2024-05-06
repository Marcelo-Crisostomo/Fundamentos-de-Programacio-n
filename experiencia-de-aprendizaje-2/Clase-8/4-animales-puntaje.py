# Mostrar la pregunta y las opciones de respuesta
print("¿Cuál de los siguientes animales vive en el agua?")
print("1. Perro")
print("2. Cocodrilo")
print("3. Conejo")
print("4. Tiburón")

# Solicitar al usuario que ingrese su respuesta
respuesta = input("Ingrese el número de su respuesta: ")

# Inicializar el puntaje en 0
puntaje = 0

# Verificar la respuesta y asignar el puntaje correspondiente
if respuesta == "2":
    puntaje += 0.5
elif respuesta == "4":
    puntaje += 1.0

# Mostrar el puntaje obtenido
print("Su puntaje es:", puntaje)
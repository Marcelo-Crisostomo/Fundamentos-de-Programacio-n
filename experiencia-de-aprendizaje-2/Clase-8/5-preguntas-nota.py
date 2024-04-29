# Inicializar el puntaje en 0
puntaje = 0

# Pregunta 1
print("Pregunta 1: ¿Quién es el protagonista de la serie 'The Mandalorian'?")
print("1. Luke Skywalker")
print("2. Din Djarin")
print("3. Han Solo")
print("4. Boba Fett")
respuesta1 = input("Ingrese el número de su respuesta: ")
if respuesta1 == "2":
    puntaje += 1

# Pregunta 2
print("Pregunta 2: ¿En qué año se estrenó la película 'Avengers: Endgame'?")
print("1. 2018")
print("2. 2019")
print("3. 2020")
print("4. 2021")
respuesta2 = input("Ingrese el número de su respuesta: ")
if respuesta2 == "2":
    puntaje += 1

# Pregunta 3
print("Pregunta 3: ¿Cuál es el nombre del personaje principal de la serie 'Stranger Things'?")
print("1. Mike Wheeler")
print("2. Dustin Henderson")
print("3. Eleven")
print("4. Will Byers")
respuesta3 = input("Ingrese el número de su respuesta: ")
if respuesta3 == "3":
    puntaje += 1

# Calcular la nota basada en el puntaje obtenido
if puntaje == 3:
    nota = "Excelente"
elif puntaje == 2:
    nota = "Bueno"
elif puntaje == 1:
    nota = "Regular"
else:
    nota = "Necesita mejorar"

# Mostrar el puntaje y la nota obtenidos
print("Su puntaje es:", puntaje)
print("Su nota es:", nota)
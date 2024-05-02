import random  # Importamos el módulo random para generar la jugada aleatoria de la computadora

opciones = ["piedra", "papel", "tijera"]  # Creamos una lista con las posibles jugadas

jugada = input("Elige: piedra, papel o tijera: ")  # Pedimos al usuario que ingrese su jugada

if jugada in opciones:  # Verificamos si la jugada del usuario está en la lista de opciones válidas
    computadora = random.choice(opciones)  # Generamos la jugada aleatoria de la computadora
    print(f"La computadora eligió: {computadora}")  # Mostramos la jugada de la computadora

    if jugada == computadora:  # Si las jugadas son iguales, es un empate
        print("¡Empate!")
    elif (jugada == "piedra" and computadora == "tijera") or \
         (jugada == "papel" and computadora == "piedra") or \
         (jugada == "tijera" and computadora == "papel"):  # Si el usuario gana según las reglas del juego
        print("¡Ganaste!")
    else:  # En cualquier otro caso, el usuario pierde
        print("¡Perdiste!")
else:  # Si la jugada del usuario no es válida
    print("Jugada no válida. ¡Intenta de nuevo!")
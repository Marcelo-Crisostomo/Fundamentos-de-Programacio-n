# Adivinar un número secreto generado aleatoriamente
import random
numero_secreto = random.randint(1, 100)
# Generamos un número aleatorio entre 1 y 100 utilizando la función random.randint()
intentos = 0  # Variable para llevar la cuenta de los intentos realizados
while True:
    # Este ciclo while se ejecutará hasta que el usuario adivine el número secreto
    intento = int(input("Ingrese un número entre 1 y 100: "))
    # Solicitamos al usuario que ingrese un número en cada iteración
    intentos += 1
    # Incrementamos el contador de intentos en cada iteración
    if intento < numero_secreto:
        print("El número ingresado es menor al número secreto. Intente nuevamente.")
    elif intento > numero_secreto:
        print("El número ingresado es mayor al número secreto. Intente nuevamente.")
    else:
        print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intentos. el número secreto es {numero_secreto}")
        break  # Si el usuario adivina el número secreto, salimos del ciclo utilizando break

print("Fin del juego.")
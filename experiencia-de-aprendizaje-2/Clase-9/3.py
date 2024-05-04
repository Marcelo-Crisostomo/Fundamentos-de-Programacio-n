# Inicializar la posición del jugador
posicion = 0

# Ciclo principal del juego
while True:
    # Mostrar la posición actual del jugador
    print("Posición actual:", posicion)
    
    # Solicitar al usuario la acción a realizar
    accion = input("Ingrese 'a' para ir a la izquierda, 'd' para ir a la derecha, 'w' para ir hacia adelante, o 'q' para salir: ")
    
    # Actualizar la posición según la acción ingresada
    if accion == 'a':
        posicion -= 1
    elif accion == 'd':
        posicion += 1
    elif accion == 'w':
        posicion += 10
    elif accion == 'q':
        break
    else:
        print("Acción inválida. Intente nuevamente.")
# Saldo inicial en cuenta
saldo = 100000#Loop principal del programa
while True:
# Mostrar menú
    print("Bienvenido al Banco DUOC UC, seleccione una opción")
    print("1. Consultar Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")
    # Solicitar opción al usuario
    opcion = input("Selecciona una opción (1-3):")
    # Realizar acciones según la opción seleccionada
    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    elif opcion == "2":
        print(f"Has retirado $ 1000")
    elif opcion == "3":
        print("Gracias por utilizar el Cajero.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

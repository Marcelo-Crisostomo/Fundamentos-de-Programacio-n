while True:
    print("Menú de Opciones:")
    print("1. Realizar acción 1")
    print("2. Realizar acción 2")
    print("3. Salir")
    opcion = input("Selecciona una opción (1-3):")
    if opcion == "1":
        print("Has seleccionado la opción 1.")
        # Código para la acción 1
    elif opcion == "2":
        print("Has seleccionado la opción 2.")
        # Código para la acción 2
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.")
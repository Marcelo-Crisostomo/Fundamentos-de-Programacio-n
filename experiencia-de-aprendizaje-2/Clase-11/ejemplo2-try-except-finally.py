# Defino una función que me recibe 2 parámetros
def dividir():
    try:
        # Solicitamos al usuario que ingrese el primer número y lo convertimos a tipo float
        numero1 = float(input("Ingresa el primer númerillo: "))

# Solicitamos al usuario que ingrese el segundo número y lo convertimos a tipo float
        numero2 = float(input("Ingresa el segundo númerillo: "))
        # Realizamos la división
        resulado = numero1 / numero2
        # Imprimimos el resultado de la división con formato de número entero
        print(f"El resultado de la división es: {resulado:.0f}")
    except ZeroDivisionError:
        # Si se intenta dividir por 0, capturamos la excepción ZeroDivisionError
        # Imprimimos un mensaje indicando que no se puede dividir por cero
        print("No seas menso, no se puede dividir por cero 0")
    except ValueError:
        # Si se ingresan letras en vez de números, capturamos la excepción TypeError
        # Imprimimos un mensaje indicando que los valores ingresados deben ser números
        print("Los valores ingresados deben ser números")
    else:
        # Si no se produce ninguna excepción, se ejecuta este bloque
        # Imprimimos un mensaje indicando que la división se ejecutó correctamente
        print("la división se ejecutó correctamente")
    finally:
        # Este bloque siempre se ejecuta, pase lo que pase
        # Imprimimos un mensaje indicando el fin del programa
        print("Fin del programita")



# Llamamos a la función dividir pasando los números ingresados como argumentos
dividir()
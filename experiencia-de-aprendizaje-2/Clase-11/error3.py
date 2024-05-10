try:
    # Solicitar al usuario dos números
    numerador = float(input("Ingrese el numerador (un número): "))
    divisor = float(input("Ingrese el divisor (un número diferente de cero): "))

    # Verificar si el divisor es cero
    if divisor == 0:
        raise ValueError("¡Error! El divisor no puede ser cero.")

    # Realizar la división
    resultado = numerador / divisor

    # Mostrar el resultado
    print(f"El resultado de la división es: {resultado}")

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Fin del programa.")
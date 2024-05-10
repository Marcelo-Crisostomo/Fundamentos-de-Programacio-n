# Calculadora básica con manejo de excepciones
while True:
    try:
        numero1 = float(input("Ingrese el primer número: "))
        # Solicitamos al usuario que ingrese el primer número
        numero2 = float(input("Ingrese el segundo número: "))
        # Solicitamos al usuario que ingrese el segundo número
        
        operacion = input("Ingrese la operación (+, -, *, /): ")
        # Solicitamos al usuario que ingrese la operación a realizar
        
        if operacion == "+":
            resultado = numero1 + numero2
        elif operacion == "-":
            resultado = numero1 - numero2
        elif operacion == "*":
            resultado = numero1 * numero2
        elif operacion == "/":
            resultado = numero1 / numero2
        else:
            raise ValueError("Operación inválida. Debe ingresar +, -, * o /.")
            # Si la operación ingresada no es válida, lanzamos una excepción ValueError con un mensaje de error
        
        print(f"El resultado de la operación es: {resultado}")
        # Imprimimos el resultado de la operación
        
        continuar = input("¿Desea realizar otra operación? (s/n): ")
        # Preguntamos al usuario si desea realizar otra operación
        if continuar.lower() != "s":
            break  # Si el usuario no desea realizar otra operación, salimos del ciclo
        
    except ValueError as e:
        print(f"Error: {str(e)}")
        # Si se captura una excepción ValueError, imprimimos el mensaje de error
    
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        # Si se intenta dividir entre cero, capturamos la excepción ZeroDivisionError y mostramos un mensaje de error
    
    except:
        print("Ocurrió un error inesperado.")
        # Si ocurre cualquier otra excepción no especificada, capturamos la excepción genérica y mostramos un mensaje de error

print("Fin del programa.")
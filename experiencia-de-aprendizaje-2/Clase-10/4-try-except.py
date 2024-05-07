try:
    # El bloque 'try' se utiliza para encapsular el código que podría generar una excepción (error).
    # En este caso, intentamos realizar una división por cero, lo cual generará un error de división por cero ('ZeroDivisionError').
    resultado = 10 / 0  # División por cero (error)
    
    # Si la división se realiza sin errores, se imprime el resultado.
    print("El resultado es:", resultado)

except ZeroDivisionError:
    # El bloque 'except' se ejecuta si ocurre una excepción del tipo especificado ('ZeroDivisionError') dentro del bloque 'try'.
    # En este caso, capturamos específicamente la excepción 'ZeroDivisionError'.
    
    # Si ocurre una división por cero, se imprime un mensaje de error indicando que no se puede dividir entre cero.
    print("Error: No se puede dividir entre cero.")
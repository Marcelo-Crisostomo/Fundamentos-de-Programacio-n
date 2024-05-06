# Calcular la suma de los números pares del 1 al 100
suma_pares = 0  # Variable para almacenar la suma de los números pares

for numero in range(1, 101):
    # El ciclo for itera desde el número 1 hasta el número 100 (inclusivo)
    if numero % 2 == 0:
        # Si el número es divisible entre 2 (es decir, es par), se ejecuta este bloque
        suma_pares += numero
        # Sumamos el número par a la variable suma_pares
        print(f"El número {numero} es par.")
        # Imprimimos un mensaje indicando que el número es par
    else:
        print(f"El número {numero} es impar.")
        # Si el número no es par, imprimimos un mensaje indicando que es impar

print(f"La suma de los números pares del 1 al 100 es: {suma_pares}")
# Imprimimos la suma total de los números pares
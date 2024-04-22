import math  # Importar el módulo math para utilizar el valor de pi

# Solicitar al usuario el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área utilizando la fórmula área = π * r ** 2
area = math.pi * radio ** 2

# Calcular el perímetro utilizando la fórmula perímetro = 2 * π * r
perimetro = 2 * math.pi * radio

# Imprimir los resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
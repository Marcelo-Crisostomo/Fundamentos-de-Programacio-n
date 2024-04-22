# Solicitar al usuario ingresar la temperatura en grados Celsius
celsius_str = input("Ingresa la temperatura en grados Celsius: ")

# Convertir el valor ingresado a un número flotante
celsius = float(celsius_str)

# Realizar la conversión de temperatura a grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Imprimir el resultado de la conversión
print("La temperatura en grados Fahrenheit es:", fahrenheit)

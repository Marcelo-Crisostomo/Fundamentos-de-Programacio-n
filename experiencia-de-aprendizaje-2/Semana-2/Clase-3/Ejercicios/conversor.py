# Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit utilizando la fórmula F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Convertir a grados Kelvin utilizando la fórmula K = C + 273.15
kelvin = celsius + 273.15

# Imprimir los resultados
print(f"{celsius}°C equivale a {fahrenheit}°F y {kelvin}K")
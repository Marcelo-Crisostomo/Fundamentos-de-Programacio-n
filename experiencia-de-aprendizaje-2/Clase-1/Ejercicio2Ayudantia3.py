#Solicitar al usuario ingresar su año de nacimiento
anio_nacimiento_str = input("Ingresa tu año de nacimiento: ")

# Convertir el valor ingresado a un número entero
anio_nacimiento = int(anio_nacimiento_str)

# Solicitar al usuario indicar si ya ha tenido su cumpleaños este año
cumpleanios_pasado = input("¿Ya ha tenido su cumpleaños este año? (responde 'si' o 'no'): ")

# Obtener el año actual
anio_actual = 2024  # Asumiendo el año actual como 2024

# Calcular la edad actual del usuario
if cumpleanios_pasado.lower() == 'si':
    edad = anio_actual - anio_nacimiento
else:
    edad = anio_actual - anio_nacimiento - 1

# Imprimir la edad actual del usuario
print("Tu edad actual es:", edad, "años")

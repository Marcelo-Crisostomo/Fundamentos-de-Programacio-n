# Solicitar al usuario la cantidad de pasajes a vender
cantidad_pasajes = int(input("Ingrese la cantidad de pasajes a vender: "))

# Inicializar la variable totalIngresos en 0
totalIngresos = 0

# Utilizar un bucle for para iterar sobre la cantidad de pasajes
for i in range(cantidad_pasajes):
    # Dentro del bucle, solicitar al usuario el precio de cada pasaje
    while True:
        try:
            precio_pasaje = float(input(f"Ingrese el precio del pasaje {i+1}: "))
            break  # Si el valor ingresado es válido, salir del bucle while
        except ValueError:
            # Si el usuario ingresa un valor no numérico, mostrar un mensaje de error
            print("Error: Debe ingresar un valor numérico válido.")
    
    # Acumular el precio del pasaje en la variable totalIngresos
    totalIngresos += precio_pasaje

# Imprimir el total de ingresos por la venta de pasajes
print(f"El total de ingresos por la venta de {cantidad_pasajes} pasajes es: {totalIngresos:.0f}")
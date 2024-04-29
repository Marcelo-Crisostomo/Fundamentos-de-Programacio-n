# Solicitar al usuario que ingrese el peso del paquete en kilogramos
peso = float(input("Ingrese el peso del paquete en kilogramos: "))

# Verificar el peso del paquete y calcular el costo de envío correspondiente
if peso <= 1:
    # Si el peso es menor o igual a 1 kg, el costo de envío es de $5
    costo_envio = 5
elif peso <= 5:
    # Si el peso es mayor a 1 kg pero menor o igual a 5 kg, el costo de envío es de $10
    costo_envio = 10
elif peso <= 10:
    # Si el peso es mayor a 5 kg pero menor o igual a 10 kg, el costo de envío es de $15
    costo_envio = 15
else:
    # Si el peso es mayor a 10 kg, el costo de envío es de $20
    costo_envio = 20

# Mostrar el costo de envío
print("Costo de envío: $", costo_envio)
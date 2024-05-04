# Solicitar al usuario los datos obligatorios
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

# Verificar si todos los campos están completos
if nombre and apellido and direccion and telefono:
    # Procesar el pago si todos los campos están completos
    print("Pago procesado correctamente")
else:
    # Mostrar un mensaje de error si faltan campos obligatorios
    print("Error: Por favor complete todos los campos obligatorios")
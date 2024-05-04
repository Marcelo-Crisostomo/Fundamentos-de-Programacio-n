# Diccionario con los precios de las pizzas
precios = {
    "Margarita": 10000,
    "Cuatro Quesos": 12000,
    "Napolitana": 12000,
    "Pepperoni": 14000,
    "Hawaiana": 14000
}

# Solicitar al usuario el tipo de pizza
tipo_pizza = input("Ingrese el tipo de pizza que desea (Margarita, Cuatro Quesos, Napolitana, Pepperoni, Hawaiana): ")

# Verificar si el tipo de pizza está en el diccionario de precios
if tipo_pizza in precios:
    # Obtener el precio de la pizza seleccionada
    precio_pizza = precios[tipo_pizza]
    
    # Calcular el impuesto (asumiendo un impuesto del 10%)
    impuesto = precio_pizza * 0.1
    
    # Calcular el total (neto + impuesto)
    total = precio_pizza + impuesto
    
    # Imprimir los valores del pedido
    print("Neto:", precio_pizza)
    print("Impuesto:", impuesto)
    print("Total:", total)
else:
    # Mostrar un mensaje de error si el tipo de pizza no está disponible
    print("Tipo de pizza no válido. Por favor, seleccione una pizza disponible.")
# Solicitar al usuario el precio original y el porcentaje de descuento
precio_original = float(input("Ingresa el precio original del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento (sin el símbolo %): "))

# Calcular el precio final después de aplicar el descuento
descuento_monto = precio_original * (descuento / 100)
precio_final = precio_original - descuento_monto

# Imprimir el resultado
print(f"El precio final después del descuento del {descuento}% es: ${precio_final:.2f}")
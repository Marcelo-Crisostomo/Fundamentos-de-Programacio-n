# Solicitar al usuario su peso en kilogramos y altura en metros
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Calcular el IMC utilizando la fórmula IMC = peso / (altura ** 2)
imc = peso / (altura ** 2)

# Imprimir el resultado del IMC con dos decimales
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
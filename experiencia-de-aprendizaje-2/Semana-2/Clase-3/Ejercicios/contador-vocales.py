# Solicitar al usuario una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Definir una lista con las vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Contar la cantidad de vocales en la cadena
contador_vocales = 0
for letra in cadena.lower():
    if letra in vocales:
        contador_vocales += 1

# Imprimir el resultado
print(f"La cadena tiene {contador_vocales} vocales.")
# Solicitar al usuario la cantidad de puntos obtenidos
puntos = int(input("Ingrese la cantidad de puntos obtenidos (0-12): "))

# Verificar en qué categoría se encuentra el alumno según los puntos
if puntos >= 0 and puntos <= 3:
    categoria = "Usted es un alumno de buen desempeño"
elif puntos >= 4 and puntos <= 6:
    categoria = "Usted es un alumno que puede mejorar"
elif puntos >= 7 and puntos <= 9:
    categoria = "Usted es un alumno con algunos desafíos"
else:
    categoria = "Usted es un alumno con muchos desafíos"

# Imprimir la categoría correspondiente
print(categoria)
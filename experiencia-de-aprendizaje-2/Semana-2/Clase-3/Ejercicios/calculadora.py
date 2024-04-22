# Solicitar al usuario tres calificaciones numéricas
calificacion1 = float(input("Ingresa la primera calificación: "))
calificacion2 = float(input("Ingresa la segunda calificación: "))
calificacion3 = float(input("Ingresa la tercera calificación: "))

# Calcular el promedio de las tres calificaciones
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# Imprimir el resultado
print(f"El promedio de las tres calificaciones es: {promedio:.2f}")
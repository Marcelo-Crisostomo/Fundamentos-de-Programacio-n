# Solicitar al usuario que ingrese las tres notas
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

# Calcular el promedio de las tres notas
promedio = (nota1 + nota2 + nota3) / 3

# Verificar si el promedio es igual o mayor a 4.0
if promedio >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")
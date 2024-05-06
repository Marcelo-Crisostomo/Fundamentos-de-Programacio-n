# Solicitar al usuario que ingrese su edad y su ingreso mensual
edad = int(input("Ingrese su edad: "))
ingreso = float(input("Ingrese su ingreso mensual: "))

# Verificar si la persona es apta para un préstamo
if edad >= 18 and edad <= 65 and ingreso >= 1000:
    # Si la edad está entre 18 y 65 años (inclusive) y el ingreso es mayor o igual a $1000
    # entonces la persona es apta para un préstamo
    apto = True
else:
    # Si no se cumplen las condiciones anteriores, la persona no es apta para un préstamo
    apto = False

# Mostrar si la persona es apta para un préstamo
if apto:
    print("Usted es apto para un préstamo.")
else:
    print("Usted no es apto para un préstamo.")
# Solicitar al usuario que ingrese su edad y si tiene licencia de conducir
edad = int(input("Ingrese su edad: "))
licencia = input("¿Tiene licencia de conducir? (s/n): ")

# Verificar si la persona puede conducir un vehículo
if edad >= 18:
    # Si la edad es mayor o igual a 18 años, se verifica si tiene licencia de conducir
    if licencia.lower() == "s":
        # Si tiene licencia de conducir, puede conducir un vehículo
        print("Usted puede conducir un vehículo.")
    else:
        # Si no tiene licencia de conducir, no puede conducir un vehículo
        print("Usted no puede conducir un vehículo. Necesita una licencia de conducir.")
else:
    # Si la edad es menor a 18 años, no puede conducir un vehículo
    print("Usted no puede conducir un vehículo. Debe ser mayor de 18 años.")
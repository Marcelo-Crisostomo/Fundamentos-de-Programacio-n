# Solicitar al usuario que ingrese el color del semáforo
color = input("Ingrese el color del semáforo (rojo, amarillo o verde): ")

# Verificar el color del semáforo y determinar la acción correspondiente
if color == "rojo":
    # Si el color es rojo, el conductor debe detenerse
    accion = "Detenerse"
elif color == "amarillo":
    # Si el color es amarillo, el conductor debe prepararse para detenerse
    accion = "Prepararse para detenerse"
elif color == "verde":
    # Si el color es verde, el conductor puede continuar
    accion = "Continuar"
else:
    # Si el color ingresado no es válido, se muestra un mensaje de error
    accion = "Color inválido"

# Mostrar la acción correspondiente al color del semáforo
print("Acción:", accion)
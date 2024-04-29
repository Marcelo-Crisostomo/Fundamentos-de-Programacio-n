# Solicitar al usuario que ingrese las calificaciones de los exámenes y el porcentaje de asistencia
examen1 = float(input("Ingrese la calificación del primer examen: "))
examen2 = float(input("Ingrese la calificación del segundo examen: "))
examen3 = float(input("Ingrese la calificación del tercer examen: "))
asistencia = float(input("Ingrese el porcentaje de asistencia: "))

# Calcular el promedio de las calificaciones de los exámenes
promedio_examenes = (examen1 + examen2 + examen3) / 3

# Verificar si el estudiante aprueba el curso
if promedio_examenes >= 70 and asistencia >= 70:
    # Si el promedio de los exámenes es mayor o igual a 70 y la asistencia es mayor o igual al 70%
    # entonces el estudiante aprueba el curso
    print("¡Felicidades! Has aprobado el curso.")
else:
    # Si no se cumplen las condiciones anteriores, el estudiante no aprueba el curso
    print("Lo siento, no has aprobado el curso.")

    if promedio_examenes < 70:
        # Si el promedio de los exámenes es menor a 70, se muestra un mensaje indicando que debe mejorar sus calificaciones
        print("Debes mejorar tus calificaciones en los exámenes.")

    if asistencia < 70:
        # Si la asistencia es menor al 70%, se muestra un mensaje indicando que debe mejorar su asistencia
        print("Debes mejorar tu asistencia a clases.")

    if promedio_examenes >= 70 and asistencia < 70:
        # Si el promedio de los exámenes es mayor o igual a 70 pero la asistencia es menor al 70%
        # se muestra un mensaje indicando que puede solicitar una consideración especial
        print("Aunque tu promedio de exámenes es aprobatorio, tu asistencia es insuficiente.")
        print("Puedes solicitar una consideración especial al profesor para aprobar el curso.")
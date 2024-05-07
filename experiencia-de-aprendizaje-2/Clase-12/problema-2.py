# Abrimos el archivo "ventas.txt" en modo lectura
with open("ventas.txt", "r") as archivo:
    # Leemos el contenido del archivo y lo dividimos por líneas
    lineas = archivo.read().splitlines()

# Abrimos el archivo "informe_ventas.txt" en modo escritura
with open("informe_ventas.txt", "w") as informe:
    # Escribimos el encabezado del informe
    informe.write("Informe de Ventas - Cafetería de Grano\n\n")
    
    # Escribimos los encabezados de las columnas
    informe.write("Día\tPan Ciabatta\tPie de Limón\tCafé\tOtros\tTotal\n")
    
    # Iteramos sobre cada línea del archivo de ventas
    for i, linea in enumerate(lineas, start=1):
        # Dividimos la línea por comas para obtener las ventas diarias de cada producto
        ventas_diarias = linea.split(",")
        
        # Calculamos el total de ventas para el día actual
        total_diario = sum(int(venta) for venta in ventas_diarias)
        
        # Escribimos las ventas diarias y el total en el informe
        informe.write(f"Día {i}\t{ventas_diarias[0]}\t\t{ventas_diarias[1]}\t\t{ventas_diarias[2]}\t{ventas_diarias[3]}\t{total_diario}\n")

print("Informe de ventas generado exitosamente.")
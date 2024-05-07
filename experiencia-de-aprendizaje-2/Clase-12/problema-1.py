# Abrimos el archivo "ventas.txt" en modo lectura
with open("ventas.txt", "r") as archivo:
    # Leemos el contenido del archivo y lo dividimos por líneas
    lineas = archivo.read().splitlines()

# Inicializamos un diccionario para almacenar las ventas de cada producto
ventas_productos = {"Pan Ciabatta": 0, "Pie de Limón": 0, "Café": 0, "Otros": 0}

# Iteramos sobre cada línea del archivo
for linea in lineas:
    # Dividimos la línea por comas para obtener las ventas diarias de cada producto
    ventas_diarias = linea.split(",")
    
    # Actualizamos las ventas de cada producto en el diccionario
    ventas_productos["Pan Ciabatta"] += int(ventas_diarias[0])
    ventas_productos["Pie de Limón"] += int(ventas_diarias[1])
    ventas_productos["Café"] += int(ventas_diarias[2])
    ventas_productos["Otros"] += int(ventas_diarias[3])

# Calculamos el total de ventas y el promedio de ventas diarias
total_ventas = sum(ventas_productos.values())
promedio_diario = total_ventas / len(lineas)

# Imprimimos los resultados
print("Ventas por producto:")
for producto, ventas in ventas_productos.items():
    print(f"{producto}: {ventas}")

print(f"\nTotal de ventas: {total_ventas}")
print(f"Promedio de ventas diarias: {promedio_diario:.2f}")
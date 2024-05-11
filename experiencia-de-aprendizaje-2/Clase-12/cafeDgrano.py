# Función para solicitar la cantidad vendida de un producto y manejar excepciones
def ingresar_cantidad(producto):
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
            if cantidad < 0:
                raise ValueError("Cantidad inválida. Ingrese un número entero positivo.")
            return cantidad
        except ValueError as error:
            print(error)

# Función para guardar el informe de ventas en un archivo de texto
def guardar_informe(informe):
    try:
        with open("informe_ventas.txt", "w") as archivo:
            archivo.write(informe)
        print("Informe de ventas guardado exitosamente.")
    except IOError:
        print("Error al guardar el informe de ventas.")
    finally:
        print("Proceso de generación de informe finalizado.")

# Diccionario con los productos y sus precios
productos = {
    "Pan ciabatta": 2000,
    "Pie de limón": 3500,
    "Café": 2200,
    "Té": 1600,
    "Alfajor": 1000
}

# Diccionario para almacenar las ventas de cada producto
ventas = {}

# Solicitar las ventas de cada producto
for producto in productos:
    cantidad = ingresar_cantidad(producto)
    ventas[producto] = cantidad

# Calcular el total de ventas por producto y el total de ventas del día
total_ventas_dia = 0
informe = "Informe de Ventas - Cafetería De Grano\n\n"

for producto, cantidad in ventas.items():
    total_ventas_producto = cantidad * productos[producto]
    informe += f"{producto}: {cantidad} unidades vendidas, total: ${total_ventas_producto}\n"
    total_ventas_dia += total_ventas_producto

informe += f"\nTotal de ventas del día: ${total_ventas_dia}"

# Imprimir el informe de ventas en la consola
print(informe)

# Guardar el informe de ventas en un archivo de texto
guardar_informe(informe)
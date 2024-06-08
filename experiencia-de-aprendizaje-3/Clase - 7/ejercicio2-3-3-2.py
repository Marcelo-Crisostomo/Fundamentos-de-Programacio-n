import csv  
import json  

ganadores = []  # Crea una lista vacía 

with open('listadoRun.csv', 'r') as file:  # Abre el archivo 'listadoRun.csv' en modo lectura
    reader = csv.DictReader(file)  # Crea un objeto DictReader para leer los datos como un diccionario
    for row in reader:  # Itera sobre cada fila del archivo CSV
        run = row['run']  # Extrae el valor de la columna 'run'
        nombre = row['nombre']  # Extrae el valor de la columna 'nombre'
        
        digitos_run = run.split('-')[0][-2:]  # Obtiene los dos últimos dígitos del run antes del dígito verificador
        
        if digitos_run in ['92', '95', '84']:  # Verifica si los dos últimos dígitos coinciden con '92', '95' o '84'
            ganadores.append(row)  # Agrega el registro a la lista 'ganadores'

with open('ganadores.json', 'w') as file:  # Abre el archivo 'ganadores.json' en modo escritura
    json.dump(ganadores, file)  # Escribe la lista 'ganadores' en formato JSON en el archivo
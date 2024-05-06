# Este es un programa de ejemplo en Python
# Declara variables y muestra cómo trabajar con tipos de datos, operadores, estructuras de control de flujo, colecciones, funciones, entrada/salida, manejo de errores, archivos, módulos, programación orientada a objetos y manejo de cadenas de texto.

# Variables y Tipos de Datos
# Para ejecutar una parte de este programa, deberás comentar las secciones que no probarás
variable_entera = 42 # Declara una variable llamada "variable_entera" y le asigna el valor entero 42
variable_decimal = 3.14 # Declara una variable llamada "variable_decimal" y le asigna el valor decimal 3.14
variable_texto = "Hola, mundo!" # Declara una variable llamada "variable_texto" y le asigna la cadena de texto "Hola, mundo!"
variable_booleana = True # Declara una variable llamada "variable_booleana" y le asigna el valor booleano True

# Operadores
resultado_suma = variable_entera + variable_decimal # Realiza la suma de "variable_entera" y "variable_decimal" y almacena el resultado en la variable "resultado_suma"
comparacion = (variable_entera > variable_decimal) # Compara si "variable_entera" es mayor que "variable_decimal" y almacena el resultado booleano en la variable "comparacion"

# Estructuras de Control de Flujo
if variable_booleana: # Si la variable "variable_booleana" es True
    print("La variable booleana es verdadera.") # Imprime el mensaje "La variable booleana es verdadera."
elif resultado_suma < 10: # Si "variable_booleana" es False y "resultado_suma" es menor que 10
    print("La suma es menor que 10.") # Imprime el mensaje "La suma es menor que 10."
else: # Si ninguna de las condiciones anteriores se cumple
    print("Ninguna de las condiciones anteriores se cumple.") # Imprime el mensaje "Ninguna de las condiciones anteriores se cumple."

# Colecciones de Datos
lista_numeros = [1, 2, 3, 4, 5] # Declara una lista llamada "lista_numeros" con los elementos enteros 1, 2, 3, 4 y 5
tupla_colores = ("rojo", "verde", "azul") # Declara una tupla llamada "tupla_colores" con los elementos de cadena de texto "rojo", "verde" y "azul"
diccionario_edades = {"Juan": 25, "María": 30, "Carlos": 22} # Declara un diccionario llamado "diccionario_edades" con claves de cadena de texto y valores enteros
conjunto_elementos = {1, 2, 3, 4, 5} # Declara un conjunto llamado "conjunto_elementos" con los elementos enteros 1, 2, 3, 4 y 5 (no se permiten duplicados)

# Funciones
def saludar(nombre): # Declara una función llamada "saludar" que toma un parámetro "nombre"
    return "¡Hola, " + nombre + "!" # Retorna una cadena de texto que contiene "¡Hola, " concatenada con el valor del parámetro "nombre" y un "!"

mensaje_saludo = saludar("Estudiante") # Llama a la función "saludar" pasando el argumento "Estudiante" y almacena el resultado en la variable "mensaje_saludo"

# Entrada y Salida
nombre_usuario = input("Por favor, ingresa tu nombre: ") # Muestra el mensaje "Por favor, ingresa tu nombre: " y almacena la entrada del usuario en la variable "nombre_usuario"
print("Hola, " + nombre_usuario + "! Este es tu primer programa en Python.") # Imprime un saludo que incluye el valor de la variable "nombre_usuario"

# Manejo de Errores
try: # Inicia un bloque de código "try" para intentar ejecutar una sección de código que puede generar un error
    resultado_division = 0 / 0 # Intenta dividir 0 entre 0, lo cual generará un error de "ZeroDivisionError"
except ZeroDivisionError: # Si ocurre un error de tipo "ZeroDivisionError" (división por cero)
    print("¡Error! No se puede dividir por cero.") # Imprime el mensaje "¡Error! No se puede dividir por cero."
finally: # Este bloque se ejecutará independientemente de si ocurrió un error o no
    print("Bloque 'finally': Este código se ejecuta siempre, haya o no haya errores.") # Imprime el mensaje indicando que este código se ejecutará siempre

# Trabajo con Archivos
with open("archivo.txt", "w") as archivo: # Abre un archivo llamado "archivo.txt" en modo escritura ("w") y lo asigna a la variable "archivo"
    archivo.write("¡Hola desde un archivo!") # Escribe la cadena de texto "¡Hola desde un archivo!" en el archivo

# Módulos y Bibliotecas
import math # Importa el módulo "math", que proporciona funciones matemáticas
raiz_cuadrada = math.sqrt(16) # Calcula la raíz cuadrada de 16 utilizando la función "sqrt" del módulo "math" y almacena el resultado en la variable "raiz_cuadrada"

# Programación Orientada a Objetos
class MiClase: # Declara una clase llamada "MiClase"
    def __init__(self, atributo): # Define el método constructor "__init__" que se ejecuta al crear una instancia de la clase y toma un parámetro "atributo"
        self.atributo = atributo # Asigna el valor del parámetro "atributo" al atributo de instancia "self.atributo"

    def mostrar_atributo(self): # Define un método llamado "mostrar_atributo" que no toma parámetros
        print("El valor del atributo es:", self.atributo) # Imprime el mensaje "El valor del atributo es: " seguido del valor del atributo de instancia "self.atributo"

# Manejo de Cadenas (Strings)
longitud_cadena = len("Python") # Calcula la longitud de la cadena de texto "Python" utilizando la función "len" y almacena el resultado en la variable "longitud_cadena"
mayusculas = "hola".upper() # Convierte la cadena de texto "hola" a mayúsculas utilizando el método "upper" y almacena el resultado en la variable "mayusculas"
minusculas = "HOLA".lower() # Convierte la cadena de texto "HOLA" a minúsculas utilizando el método "lower" y almacena el resultado en la variable "minusculas"
reemplazo = "python es divertido".replace("divertido", "increíble") # Reemplaza la subcadena "divertido" por "increíble" en la cadena "python es divertido" utilizando el método "replace" y almacena el resultado en la variable "reemplazo"
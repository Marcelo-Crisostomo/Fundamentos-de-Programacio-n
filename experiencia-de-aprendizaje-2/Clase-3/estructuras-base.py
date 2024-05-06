# Este es un programa de ejemplo en Python.
# Para ejecutar una parte de este programa, deberás comentar las secciones que no proba-rás

# Variables y Tipos de Datos.
# Aquí, se han creado variables que almacenan un número entero, 
# un número decimal, una cadena de texto y un valor booleano.
variable_entera = 42  # Entero
variable_decimal = 3.14  # Decimal
variable_texto = "Hola, mundo!"  # Cadena de texto
variable_booleana = True  # Valor booleano

#Números compejos 
numeroComplejo = 1j  # Crea un número complejo con parte real 0 y parte imaginaria 1
print(type(numeroComplejo))  # Imprime el tipo de dato de numeroComplejo (complex)

#Datos de tipo rango
rango = range(9)  # Crea un objeto de tipo rango que representa la secuencia de números del 0 al 8
#Mostrar rango:
print(rango)  # Imprime el objeto rango

#Mostar el tipo de dato de rango:
print(type(rango))  # Imprime el tipo de dato de rango (range)

"""
Frozenset: es un tipo de colección inmutable que es similar a un set regular, pero con la diferencia principal de que los elementos de un frozenset no se pueden modificar después de su creación. Es decir, no se pueden agregar, eliminar o cambiar elementos una vez que el frozenset ha sido creado.
"""
frutas = frozenset({"Arándanos", "Manzanas", "Sandía"})  # Crea un frozenset con los elementos "Arándanos", "Manzanas" y "Sandía"
#mostrar frutas:
print(frutas)  # Imprime el frozenset frutas
#mostrar que tipo de dato es fruta:
print(type(frutas))  # Imprime el tipo de dato de frutas (frozenset)

"""Bytes:
Es un tipo de dato inmutable, lo que significa que una vez creado, su contenido no puede ser modificado.
Representa una secuencia de bytes (números enteros del 0 al 255).
Se puede crear a partir de una cadena de caracteres, una lista de enteros o un objeto bytes existente.
Se utiliza comúnmente para almacenar y manipular datos binarios, como archivos o transmisiones de red.
"""
# Crear un objeto bytes a partir de una cadena de caracteres
b = bytes("Hola", "utf-8")  # Crea un objeto bytes a partir de la cadena "Hola" utilizando la codificación utf-8
print(b)  # Salida: b'Hola'

# Crear un objeto bytes a partir de una lista de enteros
b = bytes([72, 111, 108, 97])  # Crea un objeto bytes a partir de una lista de enteros que representan los valores ASCII de "Hola"
print(b)  # Salida: b'Hola'

"""
Es un tipo de dato mutable, lo que significa que su contenido puede ser modificado después de crearlo.
También representa una secuencia de bytes (números enteros del 0 al 255).
Se puede crear a partir de una cadena de caracteres, una lista de enteros, un objeto bytes existente o un objeto bytearray existente.
Se utiliza cuando se necesita manipular datos binarios de forma dinámica, como en la lectura y escritura de flujos de datos.
"""
# Crear un objeto bytearray a partir de una cadena de caracteres
b = bytearray("Hola", "utf-8")  # Crea un objeto bytearray a partir de la cadena "Hola" utilizando la codificación utf-8
print(b)  # Salida: bytearray(b'Hola')

# Modificar el contenido del objeto bytearray
b[0] = 77  # Reemplaza el primer byte del bytearray por el valor 77 (ASCII de 'M')
print(b)  # Salida: bytearray(b'Mola')

'''
Abecedario en Byte
A: 65
B: 66
C: 67
D: 68
E: 69
F: 70
G: 71
H: 72
I: 73
J: 74
K: 75
L: 76
M: 77
N: 78
O: 79
P: 80
Q: 81
R: 82
S: 83
T: 84
U: 85
V: 86
W: 87
X: 88
Y: 89
Z: 90

a: 97
b: 98
c: 99
d: 100
e: 101
f: 102
g: 103
h: 104
i: 105
j: 106
k: 107
l: 108
m: 109
n: 110
o: 111
p: 112
q: 113
r: 114
s: 115
t: 116
u: 117
v: 118
w: 119
x: 120
y: 121
z: 122
'''

"""
Memoryview es un tipo de dato que permite acceder y manipular de forma eficiente la memoria subyacente de un objeto.
"""

# Crear un bytearray
datos = bytearray(b'Python')  # Crea un objeto bytearray con la cadena 'Python'

# Crear una vista de memoria
vista = memoryview(datos)  # Crea una vista de memoria sobre el objeto datos

# Acceder a un elemento
print(vista[0])  # Imprime el valor ASCII del primer byte del objeto datos (80, que corresponde a 'P')

# Modificar un elemento
vista[0] = 74  # Modifica el primer byte del objeto datos a través de la vista de memoria, cambiándolo a 74 (ASCII de 'J')

# La modificación se refleja en el objeto original
print(datos)  # Imprime el objeto datos modificado a través de la vista de memoria (bytearray(b'Jython'))

"""
None: Es un tipo de dato único que representa la ausencia de valor en Python.
"""

# Inicializar una variable con None
mi_variable = None  # Asigna el valor None a la variable mi_variable
print(mi_variable)  # Imprime None

# Operadores
# En este caso, resultado_suma almacena el resultado de 
# sumar variable_entera y variable_decimal, y comparacion 
# almacena el resultado de comparar si variable_entera es 
# mayor que variable_decimal.
resultado_suma = variable_entera + variable_decimal  # Suma las variables variable_entera y variable_decimal y almacena el resultado en resultado_suma
comparacion = (variable_entera > variable_decimal)  # Compara si variable_entera es mayor que variable_decimal y almacena el resultado en comparacion

# Entrada y Salida
nombre_usuario = input("Por favor, ingresa tu nombre: ")  # Solicita al usuario que ingrese su nombre
print("Hola, " + nombre_usuario + "! Este es tu primer programa en Python.")  # Imprime un saludo con el nombre ingresado por el usuario

# Estructuras de Control de decisiones
# Se utiliza una estructura if-elif-else para tomar decisiones basadas en condiciones
if variable_booleana:  # Si variable_booleana es True
    print("La variable booleana es verdadera.")  # Imprime este mensaje
elif resultado_suma < 10:  # Si la condición anterior no se cumple y resultado_suma es menor a 10
    print("La suma es menor que 10.")  # Imprime este mensaje
else:  # Si ninguna de las condiciones anteriores se cumple
    print("Ninguna de las condiciones anteriores se cumple.")  # Imprime este mensaje

# Funciones
# Se define una función saludar() y se la utiliza para crear un 
# mensaje de saludo personalizado
def saludar(nombre):  # Define una función llamada saludar que toma un parámetro nombre
    return "¡Hola, " + nombre + "!"  # Retorna un saludo con el nombre proporcionado

mensaje_saludo = saludar("Estudiante")  # Llama a la función saludar con el argumento "Estudiante" y almacena el resultado en mensaje_saludo

# Manejo de Errores
try:  # Bloque try para intentar ejecutar código que puede generar una excepción
    resultado_division = 0 / 0  # Intenta dividir 0 entre 0, lo cual generará una excepción ZeroDivisionError
except ZeroDivisionError:  # Si ocurre una excepción ZeroDivisionError, se ejecuta este bloque
    print("¡Error! No se puede dividir por cero.")  # Imprime un mensaje de error
finally:  # El bloque finally se ejecuta siempre, independientemente de si ocurrió una excepción o no
    print("Bloque 'finally': Este código se ejecuta siempre, haya o no haya errores.")  # Imprime un mensaje

# Trabajo con Archivos
with open("archivo.txt", "w") as archivo:  # Abre un archivo llamado "archivo.txt" en modo escritura
    archivo.write("¡Hola desde un archivo!")  # Escribe el texto "¡Hola desde un archivo!" en el archivo

# Módulos y Bibliotecas
import math  # Importa el módulo math
raiz_cuadrada = math.sqrt(16)  # Calcula la raíz cuadrada de 16 utilizando la función sqrt del módulo math

# Programación Orientada a Objetos
class MiClase:  # Define una clase llamada MiClase
    def __init__(self, atributo):  # Constructor de la clase que toma un parámetro atributo
        self.atributo = atributo  # Asigna el valor de atributo al atributo de instancia self.atributo

    def mostrar_atributo(self):  # Método de la clase
        print("El valor del atributo es:", self.atributo)  # Imprime el valor del atributo de instancia self.atributo

# Manejo de Cadenas (Strings)
longitud_cadena = len("Python")  # Calcula la longitud de la cadena "Python" y la almacena en longitud_cadena
mayusculas = "hola".upper()  # Convierte la cadena "hola" a mayúsculas y la almacena en mayusculas
minusculas = "HOLA".lower()  # Convierte la cadena "HOLA" a minúsculas y la almacena en minusculas
reemplazo = "python es divertido".replace("divertido", "increíble")  # Reemplaza la subcadena "divertido" por "increíble" en la cadena "python es divertido" y almacena el resultado en reemplazo


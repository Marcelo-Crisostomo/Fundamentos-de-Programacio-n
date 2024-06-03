import tkinter as tk  # Importa el módulo tkinter para crear la interfaz gráfica
import requests  # Importa el módulo requests para hacer solicitudes HTTP a la API
from io import BytesIO  # Importa BytesIO para manejar datos binarios en memoria
from PIL import Image, ImageTk  # Importa las clases Image e ImageTk de PIL para manipular imágenes

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()  # Obtiene el nombre del Pokémon ingresado por el usuario y lo convierte a minúsculas
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"  # Construye la URL de la API para obtener la información del Pokémon
    
    response = requests.get(url)  # Realiza una solicitud GET a la API usando la URL construida
    
    if response.status_code == 200:  # Verifica si la solicitud fue exitosa (código de estado 200)
        data = response.json()  # Convierte la respuesta JSON en un diccionario de Python
        
        nombre = data["name"]  # Obtiene el nombre del Pokémon de los datos de la API
        numero = data["id"]  # Obtiene el número del Pokémon de los datos de la API
        tipos = [tipo["type"]["name"] for tipo in data["types"]]  # Obtiene los tipos del Pokémon de los datos de la API
        
        resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipos: {', '.join(tipos)}"  # Crea una cadena con la información del Pokémon
        
        imagen_url = data["sprites"]["front_default"]  # Obtiene la URL de la imagen del Pokémon de los datos de la API
        
        response_imagen = requests.get(imagen_url)  # Realiza una solicitud GET a la URL de la imagen
        imagen = Image.open(BytesIO(response_imagen.content))  # Abre la imagen utilizando BytesIO y la respuesta de la solicitud
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensiona la imagen a un tamaño de 200x200 píxeles
        foto = ImageTk.PhotoImage(imagen)  # Convierte la imagen en un objeto PhotoImage de Tkinter
        label_imagen.config(image=foto)  # Configura la etiqueta label_imagen para mostrar la imagen
        label_imagen.image = foto  # Guarda una referencia a la imagen para evitar que sea eliminada por el recolector de basura
    else:
        resultado = "No se encontró el Pokémon."  # Si la solicitud no fue exitosa, muestra un mensaje de error
        label_imagen.config(image=None)  # Elimina la imagen de la etiqueta label_imagen
    
    label_resultado.config(text=resultado)  # Configura la etiqueta label_resultado para mostrar la información del Pokémon

window = tk.Tk()  # Crea la ventana principal de la aplicación
window.title("Buscador de Pokémon")  # Establece el título de la ventana

label_pokemon = tk.Label(window, text="Ingresa el nombre de un Pokémon:")  # Crea una etiqueta con el texto indicado
label_pokemon.pack()  # Empaqueta la etiqueta en la ventana

entry_pokemon = tk.Entry(window)  # Crea un campo de entrada para ingresar el nombre del Pokémon
entry_pokemon.pack()  # Empaqueta el campo de entrada en la ventana

button_buscar = tk.Button(window, text="Buscar", command=buscar_pokemon)  # Crea un botón con el texto "Buscar" y asocia la función buscar_pokemon al hacer clic
button_buscar.pack()  # Empaqueta el botón en la ventana

label_resultado = tk.Label(window, text="")  # Crea una etiqueta vacía para mostrar el resultado de la búsqueda
label_resultado.pack()  # Empaqueta la etiqueta de resultado en la ventana

label_imagen = tk.Label(window)  # Crea una etiqueta para mostrar la imagen del Pokémon
label_imagen.pack()  # Empaqueta la etiqueta de imagen en la ventana

window.mainloop()  # Inicia el bucle principal de la ventana para que la aplicación se ejecute
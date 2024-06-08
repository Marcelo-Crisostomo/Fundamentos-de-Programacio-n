import tkinter as tk#importa el módulo tkinter para la interfaz gráfica
import requests #Importa un módulo para hacer las solicitudes http a la API
from io import BytesIO # importa IO para los datos binarios
from PIL import Image, ImageTk #para trabajar con las imágenes de los poke

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = requests.get(url)#solicitud get a la API mediante la URL

    if response.status_code == 200: #200 verifica si la solicitud fue exitosa
        data = response.json() #convierte la respuesta en un formato json()
        nombre = data["name"]# obtenemos el nombre del poke
        numero = data["id"]# número del poke
        tipos = [tipos["type"]["name"] for tipos in data["types"]]#obteniendo el tipo de poke

        resultado = f"Nombre: {nombre}\n Número: {numero}\n Tipos: {', '.join(tipos)}"#creando una cadena con saltos de línea para obtener los datos del poke

        imagen_url = data["sprites"]["front_default"]#obtener la img url con los datos de la API

        response_imagen = requests.get(imagen_url) #realiza una solicitu get a la url
        imagen = Image.open(BytesIO(response_imagen.content))#abre la img con BytesIO
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)#redimensiona
        foto = ImageTk.PhotoImage(imagen)#convierte la img a un objeto 
        label_imagen.config(image=foto)
        label_imagen.image = foto # guarda la referencia de la imágen
    else:
        resultado = "No se encontró el pokemón, debes atraparlo."
        label_imagen.config(image=None)#elimina la imágen si no encuentra el pokemon
    label_resultado.config(text=resultado)# configura la etiqueta label para mostrar la info del poke
window = tk.Tk() #creamos la ventana principal de la aplicación
window.title("Buscador tu pokemon")

label_pokemon = tk.Label(window, text="Ingresa el nombre del pokemon")
label_pokemon.pack()

entry_pokemon = tk.Entry(window)#Crea una entrada para recibir el nombre del pokemon.
entry_pokemon.pack()#empaqueta el campo

button_buscar = tk.Button(window, text="Buscar", command=buscar_pokemon)
button_buscar.pack()#Empaqueta el botón en la ventana

label_resultado = tk.Label(window, text="")#creamos una eyiqueta vacia para mostrar los resultados de la búsqueda.
label_resultado.pack()

label_imagen = tk.Label(window)#una etiqueta para mostrar el poke
label_imagen.pack()

window.mainloop()#inicia el bucle principal para que se ejecure la aplicación


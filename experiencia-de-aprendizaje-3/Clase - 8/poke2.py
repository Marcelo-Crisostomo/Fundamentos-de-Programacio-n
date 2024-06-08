import tkinter as tk  # Importa el módulo tkinter para la interfaz gráfica
import requests  # Importa el módulo requests para hacer solicitudes HTTP a la API
from io import BytesIO  # Importa BytesIO para manejar datos binarios
from PIL import Image, ImageTk  # Importa PIL para trabajar con imágenes

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower()  # Obtiene el nombre del Pokémon ingresado y lo convierte a minúsculas
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"  # Construye la URL de la API para buscar el Pokémon
    response = requests.get(url)  # Hace una solicitud GET a la API

    if response.status_code == 200:  # Verifica si la solicitud fue exitosa (código 200)
        data = response.json()  # Convierte la respuesta en un formato JSON
        nombre = data["name"]  # Obtiene el nombre del Pokémon
        numero = data["id"]  # Obtiene el número del Pokémon
        tipos = [tipo["type"]["name"] for tipo in data["types"]]  # Obtiene los tipos del Pokémon

        # Crea una cadena con los datos del Pokémon
        resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipos: {', '.join(tipos)}"

        # Obtiene la URL de la imagen del Pokémon
        imagen_url = data["sprites"]["front_default"]
        response_imagen = requests.get(imagen_url)  # Hace una solicitud GET para obtener la imagen
        imagen = Image.open(BytesIO(response_imagen.content))  # Abre la imagen con BytesIO
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensiona la imagen
        foto = ImageTk.PhotoImage(imagen)  # Convierte la imagen a un objeto PhotoImage
        label_imagen.config(image=foto)  # Configura la etiqueta para mostrar la imagen
        label_imagen.image = foto  # Guarda la referencia de la imagen

        # Obtener y mostrar las estadísticas base del Pokémon
        stats = data["stats"]
        estadisticas = "\n".join([f"{stat['stat']['name']}: {stat['base_stat']}" for stat in stats])
        resultado += f"\n\nEstadísticas Base:\n{estadisticas}"

        # Obtener y mostrar la descripción del Pokémon
        url_species = f"https://pokeapi.co/api/v2/pokemon-species/{numero}/"
        response_species = requests.get(url_species)
        if response_species.status_code == 200:
            data_species = response_species.json()
            descripcion = data_species["flavor_text_entries"][0]["flavor_text"].replace('\n', ' ').replace('\f', ' ')
            resultado += f"\n\nDescripción:\n{descripcion}"
        else:
            resultado += "\n\nDescripción no disponible."

    else:
        resultado = "No se encontró el Pokémon, debes atraparlo."  # Mensaje si no se encuentra el Pokémon
        label_imagen.config(image=None)  # Elimina la imagen si no se encuentra el Pokémon
    
    label_resultado.config(text=resultado)  # Configura la etiqueta para mostrar los resultados

def limpiar():
    entry_pokemon.delete(0, tk.END)  # Borra el texto de la entrada
    label_resultado.config(text="")  # Limpia el texto del resultado
    label_imagen.config(image=None)  # Limpia la imagen

def mostrar_pokemon_aleatorio():
    import random  # Importa el módulo random
    numero_aleatorio = random.randint(1, 898)  # Genera un número aleatorio entre 1 y 898 (número total de Pokémon)
    url = f"https://pokeapi.co/api/v2/pokemon/{numero_aleatorio}"  # Construye la URL de la API para buscar el Pokémon
    response = requests.get(url)  # Hace una solicitud GET a la API

    if response.status_code == 200:  # Verifica si la solicitud fue exitosa (código 200)
        data = response.json()  # Convierte la respuesta en un formato JSON
        nombre = data["name"]  # Obtiene el nombre del Pokémon
        numero = data["id"]  # Obtiene el número del Pokémon
        tipos = [tipo["type"]["name"] for tipo in data["types"]]  # Obtiene los tipos del Pokémon

        # Crea una cadena con los datos del Pokémon
        resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipos: {', '.join(tipos)}"

        # Obtiene la URL de la imagen del Pokémon
        imagen_url = data["sprites"]["front_default"]
        response_imagen = requests.get(imagen_url)  # Hace una solicitud GET para obtener la imagen
        imagen = Image.open(BytesIO(response_imagen.content))  # Abre la imagen con BytesIO
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)  # Redimensiona la imagen
        foto = ImageTk.PhotoImage(imagen)  # Convierte la imagen a un objeto PhotoImage
        label_imagen.config(image=foto)  # Configura la etiqueta para mostrar la imagen
        label_imagen.image = foto  # Guarda la referencia de la imagen

        # Obtener y mostrar las estadísticas base del Pokémon
        stats = data["stats"]
        estadisticas = "\n".join([f"{stat['stat']['name']}: {stat['base_stat']}" for stat in stats])
        resultado += f"\n\nEstadísticas Base:\n{estadisticas}"

        # Obtener y mostrar la descripción del Pokémon
        url_species = f"https://pokeapi.co/api/v2/pokemon-species/{numero}/"
        response_species = requests.get(url_species)
        if response_species.status_code == 200:
            data_species = response_species.json()
            descripcion = data_species["flavor_text_entries"][0]["flavor_text"].replace('\n', ' ').replace('\f', ' ')
            resultado += f"\n\nDescripción:\n{descripcion}"
        else:
            resultado += "\n\nDescripción no disponible."

    else:
        resultado = "No se encontró el Pokémon, debes atraparlo."  # Mensaje si no se encuentra el Pokémon
        label_imagen.config(image=None)  # Elimina la imagen si no se encuentra el Pokémon
    
    label_resultado.config(text=resultado)  # Configura la etiqueta para mostrar los resultados

# Creación de la ventana principal de la aplicación
window = tk.Tk()
window.title("Buscador de Pokémon")

# Agrega un fondo temático de Pokémon a la ventana principal
fondo = tk.PhotoImage(file="fondo_pokemon.png")
background_label = tk.Label(window, image=fondo)
background_label.place(relwidth=1, relheight=1)

# Crea un frame para organizar la información
frame = tk.Frame(window, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label_pokemon = tk.Label(frame, text="Ingresa el nombre del Pokémon")
label_pokemon.pack()

entry_pokemon = tk.Entry(frame)  # Crea una entrada para recibir el nombre del Pokémon
entry_pokemon.pack()  # Empaqueta la entrada

button_buscar = tk.Button(frame, text="Buscar", command=buscar_pokemon)
button_buscar.pack()  # Empaqueta el botón de búsqueda

button_limpiar = tk.Button(frame, text="Limpiar", command=limpiar)
button_limpiar.pack()  # Empaqueta el botón de limpiar

button_aleatorio = tk.Button(frame, text="Pokémon Aleatorio", command=mostrar_pokemon_aleatorio)
button_aleatorio.pack()  # Empaqueta el botón de Pokémon aleatorio

# Crea un frame para mostrar los resultados
frame_resultado = tk.Frame(window, bg='white', bd=10)
frame_resultado.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label_resultado = tk.Label(frame_resultado, text="", bg='white')  # Crea una etiqueta vacía para mostrar los resultados
label_resultado.pack()

label_imagen = tk.Label(frame_resultado, bg='white')  # Crea una etiqueta para mostrar la imagen
label_imagen.pack()

window.mainloop()  # Inicia el bucle principal para que se ejecute la aplicación

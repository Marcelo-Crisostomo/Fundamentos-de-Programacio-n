import requests

ciudad = "Nueva York"  # Cambia la ciudad a tu gusto
api_key = "a2b3b130836df2b29363946fccb90e93"  # Reemplaza con tu clave de API
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

respuesta = requests.get(url).json()

if "main" in respuesta:
    clima = respuesta["weather"][0]["description"]
    temperatura = respuesta["main"]["temp"]
    humedad = respuesta["main"]["humidity"]
    presion = respuesta["main"]["pressure"]
    viento = respuesta["wind"]["speed"]

    print(f"Clima actual en {ciudad}:")
    print(f" - Descripción: {clima}")
    print(f" - Temperatura: {temperatura:.2f} °C")
    print(f" - Humedad: {humedad}%")
    print(f" - Presión: {presion} hPa")
    print(f" - Velocidad del viento: {viento:.2f} m/s")
else:
    print("Error al obtener datos del clima.")




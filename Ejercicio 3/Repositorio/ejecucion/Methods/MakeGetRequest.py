import requests
import json

def make_get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta tiene un código de error
        return response.text  # Devuelve el contenido de la respuesta
    except requests.exceptions.RequestException as e:
        return f"Error en la solicitud: {e}"
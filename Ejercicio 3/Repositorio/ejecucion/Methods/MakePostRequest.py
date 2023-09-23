import requests
import json

def make_post_request(url, data):
    try:
        
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Lanza una excepción si la respuesta tiene un código de error
        return response.text  # Devuelve el contenido de la respuesta
    except requests.exceptions.RequestException as e:
        return f"Error en la solicitud: {e}"
from Methods.MakeGetRequest import *

# URL de ejemplo y datos para enviar en la solicitud GET

params = "luisfer"

url =  f"https://petstore.swagger.io/v2/user/{params}"

response_content = make_get_request(url)

print(response_content)
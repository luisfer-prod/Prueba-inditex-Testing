from Methods.MakeGetRequest import *

# URL de ejemplo y datos para enviar en la solicitud GET

#Los valores posibles a pasar por parámetro son: available, pending y sold

status = {"status":"available"}

url =  "https://petstore.swagger.io/v2/pet/findByStatus"

response_content = make_get_request(url,params=status)

print(response_content)
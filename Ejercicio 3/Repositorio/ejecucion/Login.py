from Methods.MakeGetRequestParams import *

# URL de ejemplo y datos para enviar en la solicitud POST

params = {"username":"luisfer", "password":"casaDigital8"}

url = "https://petstore.swagger.io/v2/user/login"

response_content = make_get_request(url,params)

print(response_content)
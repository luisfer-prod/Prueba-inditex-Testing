from Methods.MakePostRequest import *


# URL de ejemplo y datos para enviar en la solicitud GET

url = "https://petstore.swagger.io/v2/user"

data = {
  "id": 123,
  "username": "luisfer",
  "firstName": "luis fernando",
  "lastName": "rollan",
  "email": "luisfer@gmail.com",
  "password": "casaDigital8",
  "phone": "654321987",
  "userStatus": 0
}

response_content = make_post_request(url, data)

print(response_content)
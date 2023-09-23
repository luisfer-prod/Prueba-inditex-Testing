from Methods.MakePostRequest import *


# URL de ejemplo y datos para enviar en la solicitud POST
url = "https://petstore.swagger.io/v2/pet"

data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "terrier"
  },
  "name": "camilo",
  "photoUrls": [
    ""
  ],
  "tags": [
    {
      "id": 0,
      "name": "marron"
    }
  ],
  "status": "sold"
}


response_content = make_post_request(url, data)

print(response_content)
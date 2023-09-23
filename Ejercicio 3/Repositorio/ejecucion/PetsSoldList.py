from Methods.MakeGetRequestParams import *

# URL de ejemplo y datos para enviar en la solicitud GET

status = {"status":"sold"}

url =  "https://petstore.swagger.io/v2/pet/findByStatus"

response_content = make_get_request(url,params=status)

data = json.loads(response_content)

for record in data:
        record_id = record["id"]
        record_name = record["name"]
        print(f"ID: {record_id}, Name: {record_name}")

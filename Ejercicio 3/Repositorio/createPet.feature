Feature: Crear una nueva mascota en la tienda

Scenario: Crear una nueva mascota
  * def data =
    """
    {
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
    """
  * url 'https://petstore.swagger.io'
  * path '/v2/pet'
  * request data
  * method post
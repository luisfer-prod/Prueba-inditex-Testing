Feature: Crear un usuario en la tienda de mascotas

Scenario: Crear un usuario
  Given url 'https://petstore.swagger.io/v2/user'
  And request
  """
  {
    "id": 123,
    "username": "luisfer",
    "firstName": "luis fernando",
    "lastName": "rollan",
    "email": "luisfer@gmail.com",
    "password": "casaDigital8",
    "phone": "654321987",
    "userStatus": 0
  }
  """
  When method post
  Then status 200
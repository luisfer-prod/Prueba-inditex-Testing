Feature: Obtener información de un usuario en la tienda de mascotas

Scenario: Obtener información de un usuario
  Given url 'https://petstore.swagger.io/v2/user/luisfer'
  When method get
  Then status 200
  And match response ==
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
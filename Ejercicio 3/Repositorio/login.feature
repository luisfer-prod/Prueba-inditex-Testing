Feature: Realizar una solicitud GET con parámetros a la tienda de mascotas

Background:
  * url 'https://petstore.swagger.io/v2/user/login'

Scenario: Realizar una solicitud GET con parámetros
  Given path 'v2/user/login'
  And params { username: 'luisfer', password: 'casaDigital8' }
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
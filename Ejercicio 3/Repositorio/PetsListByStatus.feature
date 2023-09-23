Feature: Realizar una solicitud GET a la tienda de mascotas

Background:
  * url 'https://petstore.swagger.io/v2/pet/findByStatus'

Scenario: Realizar solicitud GET con parámetros
  Given param status = 'available'
  When method get
  Then status 200
  And match response == 
  """
  {
    id: '#number',
    name: '#string',
    status: 'available'
  }
  """
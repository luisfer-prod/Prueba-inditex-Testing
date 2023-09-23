Feature: Análisis de nombres de mascotas y ejecución de script de Python en la tienda de mascotas

  Background:
    * url 'https://petstore.swagger.io/v2/pet/findByStatus'

  Scenario: Realizar solicitud GET con parámetros, analizar nombres y ejecutar un script de Python
    Given param status = 'available'
    When method get
    Then status 200

    * def response_data = response
    * def comando = 'python ejecucion/MatchingPetsList.py'  # Reemplaza 'mi_script.py' con el nombre real de tu archivo Python
    * def resultado = karate.exec(comando)

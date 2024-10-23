Feature: CRUD Operations for Product API

Background:
    * url 'https://www.othoba.com/daily-shopping-onion-local-pack-1kg-35104' # Replace with the actual base URL for API

# Create Operation
Scenario: Create a new product
    Given path 'products'
    And request { "name": "Onion Local Pack 1kg", "price": 100, "quantity": 10 }
    When method post
    Then status 201
    And match response.name == 'Onion Local Pack 1kg'
    And match response.price == 100
    And match response.quantity == 10

# Read Operation
Scenario: Retrieve an existing product
    Given path 'products/35104' # Replace with a valid product ID
    When method get
    Then status 200
    And match response.name == 'Onion Local Pack 1kg'
    And match response.price == 100
    And match response.quantity == 10

# Update Operation
Scenario: Update an existing product
    Given path 'products/35104' # Replace with a valid product ID
    And request { "name": "Updated Onion Pack", "price": 120, "quantity": 15 }
    When method put
    Then status 200
    And match response.name == 'Updated Onion Pack'
    And match response.price == 120
    And match response.quantity == 15

# Delete Operation
Scenario: Delete an existing product
    Given path 'products/35104' # Replace with a valid product ID
    When method delete
    Then status 204

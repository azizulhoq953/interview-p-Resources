Feature: Product API Testing

Scenario: Test GET Product Page
    Given url 'https://www.othoba.com/farm-egg-loose-30pcs-combo'
    When method get
    Then status 200
    And match response contains { "product" : "Farm Egg Loose 30pcs Combo" }

Scenario: Test Product Page Content
    Given url 'https://www.othoba.com/farm-egg-loose-30pcs-combo'
    When method get
    Then status 200
    And match response contains { "price" : "#number" }
    And match response contains { "availability" : "#string" }

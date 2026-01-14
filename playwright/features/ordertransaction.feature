Feature: Order Transaction
  Tests related to the order Transaction

  Scenario Outline: Verify Order success message in order details page
    Given place the item order with <username> and <password>
    And user is on landing page
    When I login with <username> and <password>
    And navigate to orders page
    And select the orderID
    Then verify the order message is successfully displayed
    Examples:
      | username              | password        |
      | PWTest@gmail.com      | PWTestPWTest1   |
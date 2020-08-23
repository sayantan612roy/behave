Feature: OrangeHrm Login

  Scenario: Login to the OrangeHRM application with valid parameters
    Given I launch the chrome browser
    When I open the orange HRM Homepage
    And Enter the username "Admin" and password "admin123"
    And Click on login Button
    Then User must be successfully logged in to the dashboard page

  Scenario Outline: Login to the OrangeHRM application with valid parameters
    Given I launch the chrome browser
    When I open the orange HRM Homepage
    And Enter the username "<username>" and password "<password>"
    And Click on login Button
    Then User must be successfully logged in to the dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |

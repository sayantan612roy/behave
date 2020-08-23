Feature:
  Background: common steps
    Given I launch the chrome browser
    When I open the orange HRM Homepage
    And Enter the username "Admin" and password "admin123"
    And Click on login Button



  Scenario: Login to the OrangeHRM application with valid parameters
    Then User must be successfully logged in to the dashboard page


  Scenario: Search User
    When Navigate to search page
    Then search page should be displayed

  Scenario: Advanced Search User
    When Navigate to advanced search page
    Then advanced search page should be displayed
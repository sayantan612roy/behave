Feature:

  Scenario: To check if the logo is present
    Given I launch the chrome browser
    When I open the practice URL
    Then Verify the logo is present
    And Close browser


Feature: Login Screen

  Scenario: Perform a valid login
    When I enter text ${ADMIN_USER} into the element id = txtUsername
    And I enter text ${DEFAULT_PASSWORD} into the element id = txtPassword
    And I click the element by id = btnLogin
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element by id = welcome to be visible for 2 seconds
    And I expect element id = welcome to have text "Welcome Admin"


  Scenario Template: Perform a login using <test_name>
    When I enter text <username> into the element id = txtUsername
    And I enter text <password> into the element id = txtPassword
    And I click the element by id = btnLogin
    And I wait for the element by id = spanMessage to be visible for 2 seconds
    Then I expect element id = spanMessage to have text "<expected_error_message>"
    Examples:
      |test_name        |username      |password            |expected_error_message   |
      |invalid password |${ADMIN_USER} |123abc              |Invalid credentials      |
      |empty username   |${EMPTY}      |${DEFAULT_PASSWORD} |Username cannot be empty |
      |empty password   |${ADMIN_USER} |${EMPTY}            |Password cannot be empty |
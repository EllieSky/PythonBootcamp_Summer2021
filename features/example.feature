
Feature: Login Screen

  # Please don't try to execute YET
  # we still need to import test_steps into features.steps
  # and to create environments.py to instantiate BaseMethods

  Scenario: Perform a valid login
#    Given I login as ADMIN
    Given I authenticate as ADMIN
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element id=welcome to be visible for 2 seconds
    And I expect element id=welcome to have text "Welcome Admin"
    And I get the text from element id=welcome as greeting variable


  Scenario Template: Perform a login using <test_name>
    When I enter text <username> into the element id=txtUsername
    And I enter text <password> into the element id=txtPassword
    And I click the element id=btnLogin
    And I wait for the element id=spanMessage to be visible for 2 seconds
    Then I expect element id=spanMessage to have text "<expected_error_message>"
    Examples:
      |test_name       |username      |password            |expected_error_message  |
      |invalid password|${ADMIN_USER} |123abc              |Invalid credentials     |
      |empty username  |None          |${DEFAULT_PASSWORD} |Username cannot be empty|
      |empty password  |${ADMIN_USER} |None                |Password cannot be empty|



Feature: Login Screen

  # Please don't try to execute YET
  # we still need to import test_steps into features.steps
  # and to create environments.py to instantiate BaseMethods

  Scenario: Perform a valid login
    When I enter text admin into the element id=txtUsername
    And I enter text password into the element id=txtPassword
    And I click the element id=btnLogin
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element id=welcome to be visible for 2 seconds
    And I expect element id=welcome to have text "Welcome Admin"

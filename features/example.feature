
Feature: Login Screen

  # Please don't try to execute YET
  # we still need to import test_steps into features.steps
  # and to create environments.py to instantiate BaseMethods

  Scenario: Perform a valid login
    When I enter text admin into the element id=txtUsername
    And I enter text password into the element id=txtPassword
    And I click the element id=btnLogin

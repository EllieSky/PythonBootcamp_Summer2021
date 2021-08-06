
Feature: Login Screen

  Scenario: Perform a valid login
    When I enter text admin into the element id = txtUsername
    And I enter text password into the element id = txtPassword
    And I click the element by id = btnLogin
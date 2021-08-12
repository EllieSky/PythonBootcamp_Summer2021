# Home work 10
Feature: Updating password for existing user

  Scenario: Updating password for existing user by admin
    When I enter text ${ADMIN_USER} into the element id=txtUsername
    And I enter text ${DEFAULT_PASSWORD} into the element id=txtPassword
    And I click the element id=btnLogin
    Then I click the element id=menu_admin_viewAdminModule
    And I click the element xpath=//a[text()='bobboss']
    Then I click the element id=btnSave
    And I click the element id=systemUser_chkChangePassword
    And I enter text 12345Bob into the element id=systemUser_password
    And I enter text 12345Bob into the element id=systemUser_confirmPassword
    And I click the element id=btnSave
    And wait for 1 second(s) for updating database
    Then I click the element id=welcome
    And I wait for the element xpath=//a[text()='Logout'] to be visible for 2 seconds
    And I click the element xpath=//a[text()='Logout']
    Then I enter text bobboss into the element id=txtUsername
    And I enter text 12345Bob into the element id=txtPassword
    And I click the element id=btnLogin
    Then I expect element id=welcome to have text "Welcome Bob"

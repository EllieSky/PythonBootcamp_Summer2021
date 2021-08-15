Feature: Change password and verify successful login
#  Create a BDD scenario for the following:
#Login as admin
#Switch to admin tab
#Click on bobboss username
#Click Edit
#Update bob’s password
#Logout
#Login as bobboss to verify the new password works.

  Scenario:
    When I enter text ${ADMIN_USER} into the element by id=txtUsername
    And I enter text ${DEFAULT_PASSWORD} into the element by id=txtPassword
    And I click the element by id=btnLogin
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element by id=welcome to be visible for 2 seconds
    And I expect element id=welcome to have text "Welcome Admin"
    When I click the element by id=menu_admin_viewAdminModule
    Then I expect the url to contain /admin/viewSystemUsers
    When I click the element by xpath=//a[text()='bobboss']
    Then I expect the url to contain saveSystemUser?userId=
    When I click the element by id=btnSave
    When I click the element by id=systemUser_chkChangePassword
    And I enter text 12345 into the element by id=systemUser_password
    And I enter text 12345 into the element by id=systemUser_confirmPassword
    And I click the element by id=btnSave
    Then I wait for the element by xpath=//a[text()='bobboss'] to be visible for 5 seconds
    When I click the element by id=welcome
    And I wait for the element by xpath=//a[text()='Logout'] to be visible for 4 seconds
    When I click the element by xpath=//a[text()='Logout']
    Then I expect the url to contain /auth/login
    When I enter text bobboss into the element by id=txtUsername
    And I enter text 12345 into the element by id=txtPassword
    And I click the element by id=btnLogin
    Then I expect element xpath=//a[text()='Welcome Bob'] to have text "Welcome Bob"
    
    

    
Feature: Edit Bob

  Scenario: Perform user's password update
    When I enter text ${ADMIN_USER} into the element id=txtUsername
    And I enter text ${DEFAULT_PASSWORD} into the element id=txtPassword
    And I click the element id=btnLogin
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element id=welcome to be visible for 2 seconds
    And I expect element id=welcome to have text "Welcome Admin"

    When I click the element link text=Admin
    Then I expect the url to contain /admin/viewSystemUsers

    When I click the element link text=bobboss
    Then I expect the url to contain ?userId=192

    When I click the element id=btnSave
    And I click the element id=systemUser_chkChangePassword
    And I enter TEMPORAL RANDOM text into the element id=systemUser_password
    And I enter TEMPORAL RANDOM text into the element id=systemUser_confirmPassword
    And I click the element id=btnSave
    Then I wait for 2 second(s) for URL to contain /admin/viewSystemUsers

    When I click the element id=welcome
    And I wait for the element link text=Logout to be visible for 2 seconds
    And I click the element link text=Logout
    Then I expect the url to contain /auth/login

    When I enter text bobboss into the element id=txtUsername
    And I enter TEMPORAL RANDOM text into the element id=txtPassword
    And I click the element id=btnLogin
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element id=welcome to be visible for 2 seconds
    And I expect element id=welcome to have text "Welcome Bob"

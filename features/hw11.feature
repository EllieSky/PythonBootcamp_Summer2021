Feature:Testing different methods:def scroll_to_elem(), def goto_url, def clear_input, def replace_input_text, def get_elem_value


  Scenario: Go to url
    Given I go to url /symfony/web/index.php/admin/saveSystemUser?userId=192
    Then I expect the url to contain /symfony/web/index.php/admin/saveSystemUser?userId

  Scenario: Clear input
    When I clear input by id=txtUsername
    When I clear input by id=txtPassword
    And I click the element by id=btnLogin
    Then I expect element id=spanMessage to have text "Username cannot be empty"


  Scenario: Get element value
    Given I authenticate as ADMIN
    And I wait for the element by id=welcome to be visible for 2 seconds
    And I go to url /symfony/web/index.php/admin/saveSystemUser?userId=192
    Then I expect element id=systemUser_userName to have value "bobboss"


  Scenario: Scroll to the element
    Given I authenticate as ADMIN
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element by id=welcome to be visible for 2 seconds
    And I expect element id=welcome to have text "Welcome Admin"
    And I scroll to element by xpath=//a[text() = 'Nathan']
    And I wait for the element by xpath=//a[text() = 'Nathan'] to be visible for 4 seconds
    Then I expect element xpath=//tr[9] to have text "727186 Nathan Bush Consultant Full Time"


  Scenario: Replace input in the field
    Given I authenticate as ADMIN
    Then I expect the url to contain /pim/viewEmployeeList
    And I wait for the element by id=welcome to be visible for 2 seconds
    And I expect element id=welcome to have text "Welcome Admin"
    When I click the element by id=menu_admin_viewAdminModule
    Then I expect the url to contain /admin/viewSystemUsers
    When I click the element by xpath=//tr[@class='even']//a
    Then I expect the url to contain saveSystemUser?userId=
    When I click the element by id=btnSave
    And I replace input of element by id=systemUser_userName with text bob_boss
    When I click the element by id=btnSave
    Then I wait for the element by xpath=//tr[@class='even']//a to be visible for 5 seconds
    Then I expect element xpath=//tr[@class='even']//a to have text "bob_boss"
     When I click the element by xpath=//tr[@class='even']//a
    Then I expect the url to contain saveSystemUser?userId=
    When I click the element by id=btnSave
    And I replace input of element by id=systemUser_userName with text bobboss
    When I click the element by id=btnSave
    Then I wait for the element by xpath=//tr[@class='even']//a to be visible for 5 seconds
    Then I expect element xpath=//tr[@class='even']//a to have text "bobboss"







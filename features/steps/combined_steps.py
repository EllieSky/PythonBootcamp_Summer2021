from behave import step

from test_steps.base_methods import BaseMethods
from tests import ADMIN_USER, DEFAULT_PASSWORD


@step('I login as ADMIN')
def login(context):
    context.execute_steps('''
    When I enter text ${ADMIN_USER} into the element id=txtUsername
    And I enter text ${DEFAULT_PASSWORD} into the element id=txtPassword
    And I click the element id=btnLogin
    ''')


@step('I authenticate as ADMIN')
def login2(context):
    bm: BaseMethods = context.base_methods
    bm.enter_text(ADMIN_USER, 'id', 'txtUsername')
    bm.enter_text(DEFAULT_PASSWORD, 'id', 'txtPassword')
    bm.click_elem('id', 'btnLogin')


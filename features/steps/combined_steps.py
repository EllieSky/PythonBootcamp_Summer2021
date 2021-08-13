from behave import step
from selenium.webdriver.support.select import Select

from test_steps.base_methods import BaseMethods
from tests import ADMIN_USER, DEFAULT_PASSWORD

import re

from behave import *
use_step_matcher('re')


@step("I login as ADMIN")
def login(context):
    context.execute_steps('''
    When I enter text ${ADMIN_USER} into the element id = txtUsername
    And I enter text ${DEFAULT_PASSWORD} into the element id = txtPassword
    And I click the element by id = btnLogin
    ''')


@step('I authenticate as ADMIN')
def login2(context):
    bm: BaseMethods = context.base_methods
    bm.enter_text(ADMIN_USER, 'id', 'txtUsername')
    bm.enter_text(DEFAULT_PASSWORD, 'id', 'txtPassword')
    bm.click_elem('id', 'btnLogin')


@step('I select from element (id|xpath|link text|name)="([^"]*)?" option "([^"]*)?" by text')
def select_option(context, by, locator, option):
    bm: BaseMethods = context.base_methods
    Select(bm.find_elem(by, locator)).select_by_visible_text(option)

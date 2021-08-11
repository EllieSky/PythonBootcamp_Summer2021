from behave import *

# Possible other setup/teardown functions you can create
# before_all /  after_all
# before_feature / after_feature
# before_step / after_scenario

from selenium import webdriver

from test_steps.base_methods import BaseMethods
from tests import DOMAIN, CHROME_PATH


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(executable_path=CHROME_PATH)
    context.browser.get(DOMAIN)
    context.base_methods = BaseMethods(context.browser)


def after_scenario(context, scenario):
    context.browser.quit()

import os

from behave import *

# Possible other setup/teardown functions you can create
# before_all /  after_all
# before_feature / after_feature
# before_step / after_scenario

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from test_steps.base_methods import BaseMethods
from tests import DOMAIN, CHROME_PATH, PROJ_HOME


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(executable_path=CHROME_PATH)
    context.browser.get(DOMAIN)
    context.base_methods = BaseMethods(context.browser)


def after_scenario(context, scenario):
    browser: WebDriver = context.browser

    if scenario.status.name == 'failed':
        output_folder_path = os.path.join(PROJ_HOME, 'test_output')
        os.mkdir(output_folder_path)

        scenario_folder_path = os.path.join(output_folder_path, scenario.name.replace(" ", "_").lower())
        os.mkdir(scenario_folder_path)

        print(f'Test failed on the page with url {browser.current_url}\n')
        file = open(os.path.join(scenario_folder_path, 'page_source.html'), 'w')
        file.write(browser.page_source)
        file.close()
        browser.save_screenshot(os.path.join(scenario_folder_path, "test_screenshot.png"))
    browser.quit()

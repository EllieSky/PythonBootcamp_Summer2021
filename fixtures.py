import os
import unittest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.login import LoginPage
from test_steps.common import get_browser
from tests import DOMAIN, DEFAULT_WAIT, PROJ_HOME


class BaseFixture(unittest.TestCase):
    def setUp(self):
        self.browser = get_browser()
        self.browser.get(DOMAIN)
        self.wait = WebDriverWait(self.browser, DEFAULT_WAIT)

    def tearDown(self) -> None:
        browser = self.browser
        if self._outcome.errors[1][1]:
            output_folder_path = os.path.join(PROJ_HOME, 'test_output')
            os.mkdir(output_folder_path)

            scenario_folder_path = os.path.join(output_folder_path, self._outcome._testMethodName)
            os.mkdir(scenario_folder_path)

            print(f'Test failed on the page with url {browser.current_url}\n')
            file = open(os.path.join(scenario_folder_path, 'page_source.html'), 'w')
            file.write(browser.page_source)
            file.close()
            browser.save_screenshot(os.path.join(scenario_folder_path, "test_screenshot.png"))
        self.browser.quit()


class AdminUserAuthentication(BaseFixture):
    def setUp(self):
        super().setUp()
        LoginPage(self.browser).authenticate()
        self.wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))
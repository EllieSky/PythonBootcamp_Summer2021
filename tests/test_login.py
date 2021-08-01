import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class LoginPageTests(unittest.TestCase):
    # browser variable shared across all tests incide specific class. class
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    #cleanup after test
    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        original_url = self.browser.current_url
        authenticate(self.browser)

        # wait = WebDriverWait(self.browser, 7)
        # wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        # new_url = self.browser.current_url
        # self.assertNotEqual(original_url, new_url)
        #
        # welcome_message = self.browser.find_element(By.ID, "welcome").text
        # self.assertEqual("Welcome Admin", welcome_message)
        #
        # self.browser.find_element(By.TAG_NAME, "h1").text
        # self.assertEqual("Employee Information", self.browser.find_element(By.TAG_NAME, "h1").text)
        pass
        def test_invalid_password(self):
            pass

        def test_log_out(self):
            pass

        def test_empty(self):
            pass



    def test_invalid_password(self):
        pass

    def test_empty_password(self):
        pass

if __name__ == '__main__':
    unittest.main()

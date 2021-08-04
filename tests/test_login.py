import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        original_url = self.browser.current_url
        authenticate(self.browser)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        new_url = self.browser.current_url
        self.assertNotEqual(original_url, new_url)

        welcome_message = self.browser.find_element(By.ID, "welcome").text
        self.assertEqual("Welcome Admin", welcome_message)

        self.assertEqual("Employee Information",
                         self.browser.find_element(By.TAG_NAME, "h1").text)

    def test_invalid_password(self):
        authenticate(self.browser, 'admin', 'hello')
        wait = WebDriverWait(self.browser, 5)

        error_message = self.browser.find_element(By.ID, "spanMessage").text
        error_url_position = self.browser.current_url.find("/auth/validateCredentials")

        self.assertEqual("Invalid credentials", error_message)
        self.assertEqual(error_url_position > 0, True)

    def test_empty_password(self):
        authenticate(self.browser, 'admin', '')
        wait = WebDriverWait(self.browser, 5)

        error_message = self.browser.find_element(By.ID, "spanMessage").text
        self.assertEqual("Password cannot be empty", error_message)

    def test_empty_username(self):
        authenticate(self.browser, '', 'password')
        wait = WebDriverWait(self.browser, 5)

        error_message = self.browser.find_element(By.ID, "spanMessage").text
        self.assertEqual("Username cannot be empty", error_message)

    def test_valid_credentials_after_timeout(self):
        sleep(3600)                 # wait for 1 hour
        authenticate(self.browser)

        error_message = self.browser.find_element(By.ID, "spanMessage").text
        self.assertEqual("Csrf token validation failed", error_message)


if __name__ == '__main__':
    unittest.main()

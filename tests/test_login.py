import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        original_url = self.browser.current_url
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        new_url = self.browser.current_url
        self.assertNotEqual(original_url, new_url)

        welcome_message = self.browser.find_element(By.ID, "welcome").text
        self.assertEqual("Welcome Admin", welcome_message)

        self.assertEqual("Employee Information",
                         self.browser.find_element(By.TAG_NAME, "h1").text)


if __name__ == '__main__':
    unittest.main()

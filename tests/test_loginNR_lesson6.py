import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# from tests import CHROME
from selenium.webdriver.support.wait import WebDriverWait

from PythonBootcamp_Summer2021.tests import DOMAIN, CHROME_PATH, ADMIN_USER, DEFAULT_PASSWORD


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)


    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        original_url = self.browser.current_url
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword"). send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("pim/viewEmployeeList"))

        new_url = self.browser.current_url
        self.assertNotEqual(original_url, new_url)

        welcome_message = self.browser.find_element(By.ID, "welcome").text
        self.assertEqual("abc", welcome_message)






import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonBootcamp_Summer2021.tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class LoginPageNegativeTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)


    def test_empty_username(self):
        username = ""
        self.browser.find_element(By.ID, "txtUsername").send_keys(username, Keys.ENTER)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, "spanMessage"), "Username cannot be empty"))

    def test_empty_password(self):

        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        password = ""
        self.browser.find_element(By.ID, "txtPassword").send_keys(password, Keys.ENTER)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.text_to_be_present_in_element((By.ID, "spanMessage"), "Password cannot be empty"))

    def test_password_field_copy(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.assertNotEqual(DEFAULT_PASSWORD, self.browser.find_element(By.ID, "txtPassword").text)




    def tearDown(self) -> None:
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()

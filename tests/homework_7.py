import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class HomeworkSeven(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    # Part 1
    def test_invalid_password(self):
        original_url = self.browser.current_url
        authenticate(self.browser, username='admin', password='12345')
        self.assertEqual("Invalid credentials",
                         self.browser.find_element(By.ID, "spanMessage").text)

    def test_empty_password(self):
        original_url = self.browser.current_url
        authenticate(self.browser, username='admin', password='')
        self.assertEqual("Password cannot be empty",
                         self.browser.find_element(By.ID, "spanMessage").text)

    def test_username_password(self):
        original_url = self.browser.current_url
        authenticate(self.browser, username='test', password='password')
        self.assertEqual("Invalid credentials",
                         self.browser.find_element(By.ID, "spanMessage").text)

    def test_empty_username(self):
        original_url = self.browser.current_url
        authenticate(self.browser, username='', password='password')
        self.assertEqual("Username cannot be empty",
                         self.browser.find_element(By.ID, "spanMessage").text)

    # Part 2
    def test_sorting_by_first_name(self):
        browser = self.browser
        original_url = self.browser.current_url
        authenticate(self.browser)

        wait = WebDriverWait(self.browser, 3)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        browser.find_element(By.LINK_TEXT, "First (& Middle) Name").click()

        wait = WebDriverWait(self.browser, 3)
        wait.until(expected_conditions.url_contains("sortField=firstMiddleName&sortOrder=ASC"))

        first_name_cells = self.browser.find_elements(By.XPATH, "//tbody/tr/td[3]")
        for cell in first_name_cells:
            self.assertEqual('Admin', cell.text)

    #TODO verify sorting in alphabetical order



if __name__ == '__main__':
    unittest.main()

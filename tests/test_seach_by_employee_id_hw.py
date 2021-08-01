import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class SearchOnLandingPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
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

    def tearDown(self) -> None:
        self.browser.quit()

    def test_search_by_employee_id(self):
        employee_id = "0001"
        first_name = "Bob"
        last_name = "Boss"
        self.browser.find_element(By.ID, "empsearch_id").send_keys(employee_id)
        self.browser.find_element(By.ID, "searchBtn").click()

        search_result_employee_id = self.browser.find_element(By.LINK_TEXT, "0001").text
        self.assertEqual("0001", search_result_employee_id)

        search_result_first_name = self.browser.find_element(By.LINK_TEXT, "Bob").text
        self.assertEqual("Bob", search_result_first_name)

        search_result_last_name = self.browser.find_element(By.LINK_TEXT, "Boss").text
        self.assertEqual("Boss", search_result_last_name)

        sleep(3)



if __name__ == '__main__':
    unittest.main()

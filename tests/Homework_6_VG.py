import unittest
# from time import sleep
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonBootcamp_Summer2021.tests import DOMAIN, CHROME_PATH, ADMIN_USER, DEFAULT_PASSWORD


class LoginPageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.driver.get(DOMAIN)


    def test_valid_logging(self, expected_condition=None):
        original_url = self.driver.current_url
        self.driver.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.driver.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.driver.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        new_url = self.driver.current_url
        self.assertNotEqual(original_url, new_url)
        self.assertEqual("Employee Information", self.driver.find_element(By.TAG_NAME, "h1").text)

    def test_filter_results_by_employee_id(self):
        self.driver.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.driver.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.ID,"empsearch_id").send_keys("0001")
        self.driver.find_element(By.ID, "searchBtn").click()
        self.assertEqual("0001", self.driver.find_element(By.LINK_TEXT, "0001").text)
        self.assertEqual("Bob", self.driver.find_element(By.LINK_TEXT, "Bob").text)
        self.assertEqual("Boss", self.driver.find_element(By.LINK_TEXT, "Boss").text)
        self.driver.find_element(By.ID, "resetBtn").click()


    def test_filter_results_by_job_title(self):
        self.driver.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.driver.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.ID,"empsearch_job_title").send_keys("QA Manager")
        # sleep(3)
        self.driver.find_element(By.ID, "searchBtn").click()
        # for td in tr:
        #     self.assertEqual("QA Manager", self.driver.find_element(By.TAG_NAME, "td").text)






    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

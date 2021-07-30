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

    def test_search_by_valid_id(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword"). send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("pim/viewEmployeeList"))

        self.browser.find_element(By.ID, "empsearch_id").send_keys('0001')
        # self.browser.find_element(By.ID, "searchBtn").click()
        self.browser.find_element(By.ID, "search form").submit()
        self.browser.find_element(By.XPATH, "//tbody/tr")
        self.assertEqual(1, len(rows))

        self.assertEqual('0001', self.browser.find_element(By.XPATH, '//tbody/tr/td[2]').text)
        self.assertEqual('Bob', self.browser.find_element(By.XPATH, '//tbody/tr/td[3]').text)
        self.assertEqual('Bos', self.browser.find_element(By.XPATH, '//tbody/tr/td[4]').text)
        self.assertEqual('QA Manager', self.browser.find_element(By.XPATH, '//tbody/tr/td[5]').text)



    def test_search_by_valid_id(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword"). send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("pim/viewEmployeeList"))

        browser.find_element(By.XPATH)
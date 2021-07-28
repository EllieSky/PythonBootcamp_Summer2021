import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class SearchingById(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_id_search(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        self.browser.find_element(By.ID, "empsearch_id").send_keys("0001")
        # key "ENTER" doesn't work for search by ID function
        self.browser.find_element(By.ID, "searchBtn").click()

        expected_job_title = "QA Manager"
        expected_id = "0001"

        self.assertEqual(expected_job_title,
                         self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[5]').text)

        self.assertEqual(expected_id,
                         self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[2]/a').text)


if __name__ == '__main__':
    unittest.main()

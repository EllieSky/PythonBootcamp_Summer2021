import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures import AdminUserAuthentication
from test_steps.common import authenticate
from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class PimSearchTests(AdminUserAuthentication):

    def test_search_by_valid_id(self):
        self.browser.find_element(By.ID, 'empsearch_id').send_keys('0001')
        self.browser.find_element(By.ID, 'searchBtn').click()

        rows = self.browser.find_elements(By.XPATH, "//tbody/tr")
        self.assertEqual(1, len(rows))

        self.assertEqual('0001', self.browser.find_element(By.XPATH, '//tbody/tr/td[2]/a').text)
        self.assertEqual('Bob', self.browser.find_element(By.XPATH, '//tbody/tr/td[3]/a').text)
        self.assertEqual('Boss', self.browser.find_element(By.XPATH, '//tbody/tr/td[4]/a').text)
        self.assertEqual('QA Manager', self.browser.find_element(By.XPATH, '//tbody/tr/td[5]').text)

    def test_search_by_job_title(self):
        browser = self.browser
        # browser.find_element(By.ID, 'empsearch_job_title').send_keys("QA Manager")

        ## browser.find_element(By.ID, 'empsearch_job_title').click()
        ## browser.find_element(By.XPATH, '//*[@id="empsearch_job_title"]/option[8]').click()

        Select(browser.find_element(By.ID, 'empsearch_job_title')).select_by_visible_text("QA Manager")
        Select(browser.find_element(By.ID, 'empsearch_employee_status')).select_by_visible_text("Full Time")

        # self.browser.find_element(By.ID, 'search_form').submit()
        # OR
        self.browser.find_element(By.ID, 'searchBtn').click()

        job_title_cells = self.browser.find_elements(By.XPATH, "//tbody/tr/td[5]")
        self.assertGreater(len(job_title_cells), 0)
        for cell in job_title_cells:
            self.assertEqual('QA Manager', cell.text)

        emp_type_cells = self.browser.find_elements(By.XPATH, "//tbody/tr/td[6]")
        for cell in emp_type_cells:
            self.assertEqual('Full Time', cell.text)

        # OR

        rows = self.browser.find_elements(By.XPATH, "//tbody/tr")
        for single_row in rows:
            self.assertEqual('QA Manager', single_row.find_element(By.XPATH, ".//td[5]").text)
            self.assertEqual('Full Time', single_row.find_element(By.XPATH, ".//td[6]").text)


if __name__ == '__main__':
    unittest.main()

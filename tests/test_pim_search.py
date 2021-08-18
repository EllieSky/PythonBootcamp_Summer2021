import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from fixtures import AdminUserAuthentication
from pages.employee_information import EmployeeInformationPage


class PimSearchTests(AdminUserAuthentication):

    def test_search_by_valid_id(self):
        emp_info_page = EmployeeInformationPage(self.browser)

        emp_info_page.search_for_employee_by_id('0001')
        rows = emp_info_page.get_all_employee_table_rows()
        self.assertEqual(1, len(rows))

        emp_info = emp_info_page.get_row_info(1)
        self.assertEqual('0001', emp_info.get('id'))
        self.assertEqual('Bob', emp_info.get('first name'))
        self.assertEqual('Boss', emp_info.get('last name'))
        self.assertEqual('QA Manager', emp_info.get('job title'))

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

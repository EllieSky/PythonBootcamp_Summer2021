import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from fixtures import AdminUserAuthentication
from pages.add_employee import AddEmployeePage
from pages.employee_information import EmployeeInformationPage
from pages.job import JobPage
from pages.personal_details import PersonalDetailsPage


class CreateEmployeeTests(AdminUserAuthentication):
    def setUp(self):
        super().setUp()
        self.personal_details_page = PersonalDetailsPage(self.browser)
        self.job_page = JobPage(self.browser)
        self.add_employee_page = AddEmployeePage(self.browser)
        self.emp_info_page = EmployeeInformationPage(self.browser)

    def test_create_employee_no_creds(self):
        browser = self.browser

        emp_id = str(int(time.time() * 1000))[4:]

        self.emp_info_page.click_add_employee()

        self.assertEqual(self.add_employee_page.HEADER, self.add_employee_page.get_page_header())
        self.add_employee_page.enter_employee_details('Steve', 'Jones', emp_id)

        self.assertEqual(self.personal_details_page.HEADER, self.personal_details_page.get_page_header())

        #
        self.browser.find_element(By.XPATH, '//*[@id="sidenav"]//a[text()="Job"]').click()

        self.job_page.update_job_info('HR')

        #
        browser.find_element(By.LINK_TEXT, "PIM").click()

        self.emp_info_page.search_for_employee_by_id(emp_id)
        rows = self.emp_info_page.get_all_employee_table_rows()
        self.assertEqual(1, len(rows))

        emp_info = self.emp_info_page.get_row_info(1)
        self.assertEqual('Steve', emp_info.get('first name'))
        self.assertEqual('Jones', emp_info.get('last name'))
        self.assertEqual('HR', emp_info.get('sub unit'))

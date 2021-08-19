from selenium.webdriver.common.by import By

from fixtures import AdminUserAuthentication
from pages.employee_information import EmployeeInformationPage


class CreateEmployeeTests(AdminUserAuthentication):

    def test_create_employee_no_creds(self):
        emp_info_page = EmployeeInformationPage(self.browser)
        employee_id = emp_info_page.get_random_emp_id()
        first_name = 'Steve'
        last_name = 'Jones'
        job_sub_unit = 'HR'

        emp_info_page.create_new_employee(first_name, last_name, employee_id)
        self.assertEqual("Personal Details", emp_info_page.get_text((By.CSS_SELECTOR, ".personalDetails h1")))
        emp_info_page.change_job_sub_unit(job_sub_unit)
        emp_info_page.go_to_pim_page()
        emp_info_page.search_for_employee_by_id(employee_id)
        self.assertEqual(1, len(emp_info_page.get_all_employee_table_rows()))
        employee_info = emp_info_page.get_row_info(1)
        self.assertEqual(employee_id, employee_info.get('id'))
        self.assertEqual(first_name, employee_info.get('first name'))
        self.assertEqual(last_name, employee_info.get('last name'))
        self.assertEqual(job_sub_unit, employee_info.get('sub unit'))

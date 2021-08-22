import unittest

from fixtures import AdminUserAuthentication
from pages.add_employee import AddEmployeePage
from pages.employee_information import EmployeeInformationPage
from pages.job import JobPage
from pages.personal_details import PersonalDetailsPage


class CreateEmployeeTest(AdminUserAuthentication):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.emp_info_page = None

    def test_create_employee_no_creds(self):
        emp_info_page = EmployeeInformationPage(self.browser)
        emp_info_page.click_add_btn()

        add_emp_page = AddEmployeePage(self.browser)
        self.assertEqual("Add Employee", add_emp_page.verify_add_employee_page())
        add_emp_page.create_employee()
        employee_id = add_emp_page.create_random_emp_id()
        add_emp_page.click_save_button()

        pers_details_page = PersonalDetailsPage(self.browser)
        self.assertEqual("Personal Details", pers_details_page.verify_personal_details_page())
        pers_details_page.click_job()

        job_page = JobPage(self.browser)
        self.assertEqual("Job", job_page.verify_job_page())
        job_page.click_edit_button()
        job_page.select_sub_unit("HR")
        job_page.click_save_button()

        emp_info_page.click_pim()

        emp_info_page.search_for_employee_by_id(employee_id)

        rows = emp_info_page.get_all_employee_table_rows()
        self.assertEqual(1, len(rows))

        emp_info = emp_info_page.get_row_info(1)
        self.assertEqual(employee_id, emp_info.get('id'))
        self.assertEqual('Steve', emp_info.get('first name'))
        self.assertEqual('Jones', emp_info.get('last name'))
        self.assertEqual('HR', emp_info.get('sub unit'))


if __name__ == '__main__':
    unittest.main()

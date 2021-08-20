from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods
from tests import ADMIN_USER, DEFAULT_PASSWORD


class AddEmployeePage(BaseMethods):
    HEADER = 'Add Employee'

    page_header = (By.TAG_NAME, "h1")
    first_name_fld = (By.ID, "firstName")
    last_name_fld = (By.ID, "lastName")
    employee_id_fld = (By.ID, "employeeId")
    save_btn = (By.ID, "btnSave")

    def get_page_header(self):
        return self.find_elem(self.page_header).text

    def enter_employee_details(self, first_name=None, last_name=None, emp_id=None):
        self.enter_text(self.first_name_fld, first_name) if first_name is not None else None

        if last_name is not None:
            self.enter_text(self.last_name_fld, last_name)

        self.replace_input_text(self.employee_id_fld, emp_id) if emp_id is not None else None
        # still needs code for middle name, photo, create login details, etc.
        self.click_elem(self.save_btn)

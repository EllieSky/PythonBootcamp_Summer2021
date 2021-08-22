import time

from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods


class AddEmployeePage(BaseMethods):
    add_emp_page = (By.TAG_NAME, "h1")
    fname_fld = (By.ID, "firstName")
    lname_fld = (By.ID, "lastName")
    employee_id = (By.ID, "employeeId")
    save_btn = (By.ID, "btnSave")

    def verify_add_employee_page(self):
        return self.get_text(self.add_emp_page)

    def create_employee(self):
        self.enter_text(self.fname_fld, 'Steve')
        self.enter_text(self.lname_fld, 'Jones')

    def create_random_emp_id(self):
        emp_id = str(int(time.time() * 1000))[4:]
        self.replace_input_text(self.employee_id, emp_id)
        return emp_id

    def click_save_button(self):
        self.click_elem(self.save_btn)

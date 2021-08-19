import time
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from test_steps.base_methods import BaseMethods


class EmployeeInformationPage(BaseMethods):
    search_btn = (By.ID, 'searchBtn')
    add_btn = (By.ID, "btnAdd")
    save_btn = (By.ID, "btnSave")
    edit_btn = save_btn
    employee_id_fld = (By.ID, 'empsearch_id')
    table_row = (By.XPATH, "//tbody/tr")
    fname_text_fld = (By.ID, 'firstName')
    lname_text_fld = (By.ID, "lastName")
    emp_id_text_fld = (By.ID, "employeeId")
    job_option_menu = (By.XPATH, '//*[@id="sidenav"]//a[text()="Job"]')
    job_sub_unit_selector = (By.ID, "job_sub_unit")
    pim_page_locator = (By.LINK_TEXT, "PIM")

    def search_for_employee_by_id(self, emp_id):
        self.enter_text(self.employee_id_fld, emp_id)
        self.click_elem(self.search_btn)

    def get_all_employee_table_rows(self) -> List[WebElement]:
        return self.find_elems(self.table_row)

    def get_row_info(self, row_number):
        # row = self.find_elem(By.XPATH, f"//tbody/tr[{row_number}]")
        row = self.find_elem((By.XPATH, f"{self.table_row[1]}[{row_number}]"))
        return {
            'id':  row.find_element(By.XPATH, ".//td[2]/a").text,
            'first name': row.find_element(By.XPATH, ".//td[3]/a").text,
            'last name': row.find_element(By.XPATH, ".//td[4]/a").text,
            'job title': row.find_element(By.XPATH, ".//td[5]").text,
            'employment status': row.find_element(By.XPATH, ".//td[6]").text,
            'sub unit': row.find_element(By.XPATH, ".//td[7]").text,
            'supervisor': row.find_element(By.XPATH, ".//td[8]").text
        }

    def get_random_emp_id(self) -> str:
        return str(int(time.time() * 1000))[4:]

    def create_new_employee(self, first_name: str, last_name: str,
                            emp_id):
        self.click_elem(self.add_btn)
        self.enter_text(self.fname_text_fld, first_name)
        self.enter_text(self.lname_text_fld, last_name)
        self.find_elem(self.emp_id_text_fld).clear()
        self.enter_text(self.emp_id_text_fld, emp_id)
        self.click_elem(self.save_btn)

    def change_job_sub_unit(self, sub_unit: str = 'HR'):
        self.click_elem(self.job_option_menu)
        self.click_elem(self.edit_btn)
        Select(self.find_elem(self.job_sub_unit_selector)).select_by_visible_text(sub_unit)
        self.click_elem(self.edit_btn)

    def go_to_pim_page(self):
        self.click_elem(self.pim_page_locator)

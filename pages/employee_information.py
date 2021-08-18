from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from test_steps.base_methods import BaseMethods


class EmployeeInformationPage(BaseMethods):
    search_btn = (By.ID, 'searchBtn')
    employee_id_fld = (By.ID, 'empsearch_id')
    table_row = (By.XPATH, "//tbody/tr")

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
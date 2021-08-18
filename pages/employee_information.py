from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from test_steps.base_methods import BaseMethods, find_elems


class EmployeeInformationPage(BaseMethods):
    def search_for_employee_by_id(self, emp_id):
        self.enter_text(emp_id, By.ID, 'empsearch_id')
        self.click_elem(By.ID, 'searchBtn')

    def get_all_employee_table_rows(self) -> List[WebElement]:
        return self.find_elems(self.browser, By.XPATH, "//tbody/tr")


from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from pages.add_employee_Day13 import BasePage


class TerminationReasonsPage(BasePage):
    HEADER = 'Termination Reasons'
    PAGE_URL = '/pim/viewTerminationReasons'
    page_header = (By.XPATH, "//h1[text()='Termination Reasons']")
    add_btn = (By.ID, 'btnAdd')
    list_of_reasons = (By.CSS_SELECTOR, '.tdName')
    check_btn = (By.XPATH, "//a[text()='Missing / No - Show']/preceding::td[1]")
    delete_btn = (By.ID, 'btnDel')
    table = (By.ID, 'recordsListTable')
    success_msg = (By.CSS_SELECTOR, '.message.success')


    def click_add_btn(self):
        self.click_elem(self.add_btn)

    def get_table_of_reasons(self):
        reason_table = self.find_elem(self.table)
        return reason_table

    def get_all_elements_in_table(self) -> List[WebElement]:
        return self.find_elems(self.list_of_reasons)

    def remove_reason(self):
        self.click_elem(self.check_btn)
        self.click_elem(self.delete_btn)
        self.wait.until(EC.visibility_of_element_located(self.success_msg))

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.add_employee_Day13 import BasePage


class TerminationReasonsPage(BasePage):
    HEADER = 'Termination Reasons'
    PAGE_URL = '/pim/viewTerminationReasons'
    page_header = (By.XPATH, "//h1[text()='Termination Reasons']")
    add_btn = (By.ID, 'btnAdd')
    list_of_reasons = (By.CSS_SELECTOR, '.tdName')
    check_btn = (By.XPATH, "//a[text()='Missing / No - Show']/preceding::td[1]")
    delete_btn = (By.ID, 'btnDel')

    def click_add_btn(self):
        self.click_elem(self.add_btn)

    def get_list_of_reasons(self) -> List[WebElement]:
        reason_list = self.find_elems(self.list_of_reasons)
        return reason_list

    def remove_reason(self):
        self.click_elem(self.check_btn)
        self.click_elem(self.delete_btn)

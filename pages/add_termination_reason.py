from selenium.webdriver.common.by import By

from pages.add_employee_Day13 import BasePage


class AddTerminationReasonPage(BasePage):
    HEADER = 'Add Termination Reason'
    PAGE_URL = '/pim/viewTerminationReasons'
    reason_name = (By.ID, 'terminationReason_name')
    save_btn = (By.ID, 'btnSave')

    def add_reason(self, reason_text=None):
        self.enter_text(self.reason_name, reason_text)
        self.click_elem(self.save_btn)

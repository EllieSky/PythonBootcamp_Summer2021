from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.add_employee_Day13 import BasePage


class AddTerminationReasonPage(BasePage):
    HEADER = 'Add Termination Reason'
    PAGE_URL = '/pim/viewTerminationReasons'
    reason_name = (By.ID, 'terminationReason_name')
    save_btn = (By.ID, 'btnSave')
    success_msg = (By.CSS_SELECTOR, '.message.success')

    def add_reason(self, reason_text=None):
        self.enter_text(self.reason_name, reason_text)
        self.click_elem(self.save_btn)
        self.wait.until(EC.visibility_of_element_located(self.success_msg))

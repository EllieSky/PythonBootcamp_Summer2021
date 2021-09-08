from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.add_employee import BasePage


class TerminationReasons(BasePage):
    HEADER = 'Termination Reasons'
    PAGE_URL = '/pim/viewTerminationReasons'
    success_msg = (By.CSS_SELECTOR, '.message.success')

    page_header = (By.CSS_SELECTOR, "#recordsListDiv h1")
    add_btn = (By.ID, 'btnAdd')
    delete_btn = (By.ID, 'btnDel')
    save_btn = (By.ID, 'btnSave')
    reason_name_fld = (By.ID, 'terminationReason_name')

    def add_new_reason(self, text):
        self.click_elem(self.add_btn)
        self.enter_text(self.reason_name_fld, text)
        self.click_elem(self.save_btn)
        self.wait.until(EC.presence_of_element_located(self.success_msg))

    def remove_reason(self, text):
        self.click_elem((By.XPATH, f"//a[text()='{text}']/ancestor::tr/td[1]"))
        self.click_elem(self.delete_btn)
        self.wait.until(EC.presence_of_element_located(self.success_msg))

    def find_required_reason(self, text):
        if self.browser.find_elements(By.XPATH, f"//a[text()='{text}']"):
            return True
        else:
            return False

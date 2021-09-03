from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.add_employee import BasePage


class TerminationReasonsPage(BasePage):
    HEADER = 'Termination Reasons'
    PAGE_URL = '/pim/viewTerminationReasons'

    page_header = (By.CSS_SELECTOR, '.box.miniList>.head>h1')
    reason_name_fld = (By.ID, "terminationReason_name")
    add_reason_btn = (By.ID, "btnAdd")
    save_reason_btn = (By.ID, "btnSave")
    delete_reason_btn = (By.ID, "btnDel")
    reason_td = (By.CSS_SELECTOR, ".tdName.tdValue")
    success_msg = (By.CSS_SELECTOR, '.message.success')

    def add_new_reason(self, reason_name):
        self.click_elem(self.add_reason_btn)
        self.enter_text(self.reason_name_fld, reason_name)
        self.click_elem(self.save_reason_btn)
        self.wait.until(EC.presence_of_element_located(self.success_msg))

    def search_reason(self, reason_name):
        return self.find_elems_or_not((By.LINK_TEXT, reason_name))

    def delete_reason(self, reason_name):
        link = self.find_elem((By.LINK_TEXT, reason_name))
        checkbox = link.find_element(
            By.XPATH,
            f'//a[contains(.,"{reason_name}")]/../preceding-sibling::td[input[@class="checkbox"]]')
        checkbox.click()
        self.click_elem(self.delete_reason_btn)
        self.wait.until(EC.presence_of_element_located(self.success_msg))

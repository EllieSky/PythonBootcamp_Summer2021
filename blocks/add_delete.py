from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from test_steps.base_methods import BaseMethods


class AddDelete(BaseMethods):
    add_btn = (By.ID, 'btnAdd')
    delete_btn = (By.ID, 'btnDelete')
    delete_confirmation_dialog = (By.ID, 'deleteConfModal')
    dialog_ok_btn = (By.ID, 'dialogDeleteBtn')
    dialog_cancel_btn = (By.CLASS_NAME, 'cancel')

    def add(self):
        url = self.browser.current_url
        self.click_elem(self.add_btn)
        self.wait.until(EC.url_changes(url))

    def delete(self):
        if not self.find_elem(self.delete_btn).is_enabled():
            return
        self.click_elem(self.delete_btn)
        self.wait_for_elem_visible(self.delete_confirmation_dialog)
        self.click_elem(self.dialog_ok_btn)

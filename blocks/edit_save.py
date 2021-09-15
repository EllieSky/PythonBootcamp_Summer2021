from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from test_steps.base_methods import BaseMethods


class EditSave(BaseMethods):
    default_input = (By.CSS_SELECTOR, 'form input')
    success_msg = (By.CSS_SELECTOR, '.message.success')
    save_btn = (By.ID, "btnSave")
    edit_btn = save_btn

    def save(self):
        self.click_elem(self.save_btn)
        self.wait.until(EC.presence_of_element_located(self.success_msg))

    def edit(self):
        self.click_elem(self.edit_btn)
        self.wait.until(EC.element_to_be_clickable(self.default_input))

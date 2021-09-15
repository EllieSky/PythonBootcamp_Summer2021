from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods
from selenium.webdriver.support import expected_conditions as EC


class UploadFile(BaseMethods):
    add_attachment_btn = (By.ID, 'btnAddAttachment')
    save_attachment_btn = (By.ID, 'btnSaveAttachment')

    file_chooser_fld = (By.CSS_SELECTOR, "[type='file']")

    def choose_file(self, file_path):
        self.replace_input_text(self.file_chooser_fld, file_path)

    def upload(self):
        self.click_elem(self.save_attachment_btn)
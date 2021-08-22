from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test_steps.base_methods import BaseMethods


class JobPage(BaseMethods):
    job_page = (By.CSS_SELECTOR, ".head h1")
    edit_btn = (By.ID, "btnSave")
    sub_unit = (By.ID, "job_sub_unit")
    save_btn = (By.ID, "btnSave")

    def verify_job_page(self):
        return self.get_text(self.job_page)

    def click_edit_button(self):
        self.click_elem(self.edit_btn)

    def select_sub_unit(self, txt):
        Select(self.find_elem(self.sub_unit)).select_by_visible_text(txt)

    def click_save_button(self):
        self.click_elem(self.save_btn)

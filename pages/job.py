from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from test_steps.base_methods import BaseMethods
from tests import ADMIN_USER, DEFAULT_PASSWORD


class JobPage(BaseMethods):
    HEADER = 'Job'
    success_msg = (By.CSS_SELECTOR, '.message.success')
    page_header = (By.CSS_SELECTOR, ".head>h1")
    sub_unit_fld = (By.ID, "job_sub_unit")
    save_btn = (By.ID, "btnSave")
    edit_btn = save_btn

    def update_job_info(self, sub_unit=None):
        self.click_elem(self.edit_btn)
        self.wait.until(EC.element_to_be_clickable(self.sub_unit_fld))

        if sub_unit is not None:
            Select(self.find_elem(self.sub_unit_fld)).select_by_visible_text(sub_unit)
        # still needs all other fields added here
        self.click_elem(self.save_btn)
        self.wait.until(EC.presence_of_element_located(self.success_msg))

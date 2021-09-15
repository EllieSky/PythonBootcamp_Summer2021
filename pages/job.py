from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from blocks.edit_save import EditSave
from blocks.upload_file import UploadFile
from pages.add_employee import BasePage


class JobPage(BasePage, EditSave, UploadFile):
    HEADER = 'Job'
    PAGE_URL = '/pim/viewJobDetails/empNumber/'
    page_header = (By.CSS_SELECTOR, ".head>h1")
    sub_unit_fld = (By.ID, "job_sub_unit")
    default_input = sub_unit_fld

    def update_job_info(self, sub_unit=None):
        self.edit()
        if sub_unit is not None:
            Select(self.find_elem(self.sub_unit_fld)).select_by_visible_text(sub_unit)
        # still needs all other fields added here
        self.save()

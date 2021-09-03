from telnetlib import EC

from selenium.webdriver.common.by import By

from pages.add_employee import BasePage


class PersonalDetailsPage(BasePage):
    HEADER = 'Personal Details'
    PAGE_URL = '/pim/viewEmployee/empNumber/'

    page_header = (By.CSS_SELECTOR, ".personalDetails h1")
    middle_name_fld=(By.CSS_SELECTOR, "personalDetails h1")
    save_btn = (By.ID, "btnSave")
    edit_btn = save_btn
    success_msg = (By.CSS_SELECTOR, '.message.success')

    def edit(self):
        self.click_elem(self.edit_btn)

    def update_personal_details(self, first_name=None, middle_name=None,last_name=None,nick_name='fluf'):
        if not self.find_elem(self.first_name_fld).is_enabled():
        self.edit()
        self.replace_input_text(self.first_name_fld, first_name) if first_name is not None else None
        self.replace_input_text(self.middle_name_fld, middle_name) if middle_name is not None else None
        self.replace_input_text(self.last_name_fld, last_name) if last_name is not None else None
        self.click_elem(self.save_btn)
        self.wait.until(EC.presence_of_element_located(self.success_msg))

    def get_profile_pic_header(self):
        return self.
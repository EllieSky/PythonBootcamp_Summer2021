from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from blocks.edit_save import EditSave
from pages.add_employee import BasePage


class PersonalDetailsPage(BasePage, EditSave):
    HEADER = 'Personal Details'
    PAGE_URL = '/pim/viewEmployee/empNumber/'

    page_header = (By.CSS_SELECTOR, ".personalDetails h1")

    profile_pic_header = (By.CSS_SELECTOR, '#profile-pic h1')

    emp_number_hidden_fld = (By.ID, 'personal_txtEmpID')

    first_name_fld = (By.ID, 'personal_txtEmpFirstName')
    middle_name_fld = (By.ID, 'personal_txtEmpMiddleName')
    last_name_fld = (By.ID, 'personal_txtEmpLastName')
    nick_name_fld = (By.ID, 'personal_txtEmpNickName')

    default_input = first_name_fld

    def update_personal_details(self, first_name=None, middle_name=None, last_name=None, nick_name=None):
        if not self.find_elem(self.first_name_fld).is_enabled():
            self.edit()
        self.replace_input_text(self.first_name_fld, first_name) if first_name is not None else None
        if middle_name is not None:
            self.replace_input_text(self.middle_name_fld, middle_name)
        self.replace_input_text(self.last_name_fld, last_name) if last_name is not None else None
        self.replace_input_text(self.nick_name_fld, nick_name) if nick_name is not None else None
        self.save()

    def get_profile_pic_header(self):
        return self.get_text(self.profile_pic_header)

    def get_employee_number(self):
        return self.get_elem_value(self.emp_number_hidden_fld)

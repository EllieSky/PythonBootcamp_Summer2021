from selenium.webdriver.common.by import By

from pages.add_employee import BasePage
from tests import ADMIN_USER, DEFAULT_PASSWORD


class LoginPage(BasePage):
    HEADER = 'LOGIN Panel'
    PAGE_URL = '/auth/login'

    page_header = (By.ID, 'logInPanelHeading')
    username_fld = (By.ID, 'txtUsername')
    password_fld = (By.ID, 'txtPassword')
    login_btn = (By.ID, "btnLogin")
    error_msg = (By.ID, 'spanMessage')

    def authenticate(self, username=ADMIN_USER, password=DEFAULT_PASSWORD):
        self.enter_text(self.username_fld, username)
        self.enter_text(self.password_fld, password)
        self.click_elem(self.login_btn)

    def get_error_message(self):
        return self.find_elem(self.error_msg).text

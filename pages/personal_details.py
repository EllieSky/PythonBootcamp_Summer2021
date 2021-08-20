from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods
from tests import ADMIN_USER, DEFAULT_PASSWORD


class PersonalDetailsPage(BaseMethods):
    HEADER = 'Personal Details'

    page_header = (By.CSS_SELECTOR, ".personalDetails h1")

    def get_page_header(self):
        return self.find_elem(self.page_header).text

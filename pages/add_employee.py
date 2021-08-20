from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from menus.top_nav import TopNavMenu
from test_steps.base_methods import BaseMethods
from tests import BASE_URL


class BasePage(BaseMethods):
    page_header = (By.TAG_NAME, "h1")
    PAGE_URL = '/'

    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.top_menu = TopNavMenu(browser)

    def get_page_header(self):
        return self.find_elem(self.page_header).text

    def goto_page(self):
        self.browser.get(BASE_URL + self.PAGE_URL)


class AddEmployeePage(BasePage):
    HEADER = 'Add Employee'
    PAGE_URL = '/pim/addEmployee'

    first_name_fld = (By.ID, "firstName")
    last_name_fld = (By.ID, "lastName")
    employee_id_fld = (By.ID, "employeeId")
    save_btn = (By.ID, "btnSave")

    def enter_employee_details(self, first_name=None, last_name=None, emp_id=None):
        self.enter_text(self.first_name_fld, first_name) if first_name is not None else None

        if last_name is not None:
            self.enter_text(self.last_name_fld, last_name)

        self.replace_input_text(self.employee_id_fld, emp_id) if emp_id is not None else None
        # still needs code for middle name, photo, create login details, etc.
        self.click_elem(self.save_btn)

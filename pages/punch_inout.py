from selenium.webdriver.common.by import By

from pages.add_employee import BasePage


class PunchInOutPage(BasePage):
    HEADER = 'Punch In'
    PAGE_URL = '/attendance/punchIn'
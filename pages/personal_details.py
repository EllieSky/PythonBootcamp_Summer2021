from selenium.webdriver.common.by import By

from pages.add_employee import BasePage


class PersonalDetailsPage(BasePage):
    HEADER = 'Personal Details'
    PAGE_URL = '/pim/viewEmployee/empNumber/'

    page_header = (By.CSS_SELECTOR, ".personalDetails h1")

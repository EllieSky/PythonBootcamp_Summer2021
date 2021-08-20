from selenium.webdriver.common.by import By

from pages.add_employee import BasePage


class LocalizationPage(BasePage):
    HEADER = 'Localization'
    PAGE_URL = '/admin/localization'

    page_header = (By.ID, "localizationHeading")

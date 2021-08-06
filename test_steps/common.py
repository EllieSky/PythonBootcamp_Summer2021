from selenium.webdriver.common.by import By

from tests import ADMIN_USER, DEFAULT_PASSWORD


def authentification(browser):
    browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
    browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
    browser.find_element(By.ID, "btnLogin").click()
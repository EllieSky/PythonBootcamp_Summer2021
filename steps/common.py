from selenium.webdriver.common.by import By

from tests import ADMIN_USER, DEFAULT_PASSWORD
"""
blah
"""
#TODO blah
def authenticate(browser, username = ADMIN_USER, password=DEFAULT_PASSWORD):
    browser.find_element(By.ID, "txtUsername").send_keys(username)
    browser.find_element(By.ID, "txtPassword").send_keys(password)
    browser.find_element(By.ID, "btnLogin").click()
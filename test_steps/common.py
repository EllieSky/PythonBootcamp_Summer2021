from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests import ADMIN_USER, DEFAULT_PASSWORD, BROWSER, DriverPath


def get_browser(browser_type: str = BROWSER) -> WebDriver:
    browser: WebDriver
    if browser_type.lower() == 'chrome' or browser_type.lower() == 'googlechrome':
        browser = webdriver.Chrome(executable_path=DriverPath().CHROME)
    elif browser_type.lower() == 'firefox':
        browser = webdriver.Firefox(executable_path=DriverPath().FIREFOX)
    else:
        raise TypeError(f'Browser type "{browser_type}" is currently not supported, '
                        f'please choose one of the following: \nChrome\nFirefox')
    return browser

def authenticate(browser, username=ADMIN_USER, password=DEFAULT_PASSWORD):
    """

    Used to login into Orange HRM site

    :param password:
    :param username:
    :param browser:
    :return: None
    """
    # regular comment
    #TODO: need to add params
    browser.find_element(By.ID, "txtUsername").send_keys(username)
    browser.find_element(By.ID, "txtPassword").send_keys(password)
    browser.find_element(By.ID, "btnLogin").click()

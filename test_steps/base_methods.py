from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests import DEFAULT_WAIT


class BaseMethods:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.wait: WebDriverWait = WebDriverWait(browser, DEFAULT_WAIT)

    def find_elem(self, locator: tuple) -> WebElement:
        # return self.browser.find_element(by, locator)
        # return self.wait.until(EC.presence_of_element_located([by, locator]))
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elems(self, locator: tuple) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_elem(self, locator: tuple):
        self.find_elem(locator).click()

    def enter_text(self, locator: tuple, text):
        self.find_elem(locator).send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.find_elem(locator).text

    def wait_for_elem_visible(self, locator: tuple, seconds):
        return WebDriverWait(self.browser, int(seconds)).until(
            EC.visibility_of_element_located(locator))


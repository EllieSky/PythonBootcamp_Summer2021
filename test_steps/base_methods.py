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

    def find_elem(self, by, locator) -> WebElement:
        # return self.browser.find_element(by, locator)
        # return self.wait.until(EC.presence_of_element_located([by, locator]))
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_elems(self, by, locator) -> List[WebElement]:
        return self.browser.find_elements(by, locator)

    def click_elem(self, by, locator):
        self.find_elem(by, locator).click()

    def enter_text(self, text, by, locator):
        self.find_elem(by, locator).send_keys(text)

    def get_text(self, by, locator) -> str:
        return self.find_elem(by, locator).text

    def wait_for_elem_visible(self, by, locator, seconds):
        return WebDriverWait(self.browser, int(seconds)).until(
            EC.visibility_of_element_located((by, locator)))


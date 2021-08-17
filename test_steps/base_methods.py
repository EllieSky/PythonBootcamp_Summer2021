import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethods:
    def __init__(self, browser):
        self.browser: WebDriver = browser
        self.wait: WebDriverWait = WebDriverWait(browser, 5)
        self.temporal = None

    def find_elem(self, by, locator) -> WebElement:
        # return self.browser.find_element(by, locator)
        # return self.wait.until(EC.presence_of_element_located([by, locator]))
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click_elem(self, by, locator):
        self.find_elem(by, locator).click()

    def enter_text(self, text, by, locator):
        self.find_elem(by, locator).send_keys(text)

    def get_text(self, by, locator) -> str:
        return self.find_elem(by, locator).text

    def wait_for_elem_visible(self, by, locator, seconds):
        return WebDriverWait(self.browser, seconds).until(
            EC.visibility_of_element_located((by, locator)))

    def wait_for_url(self, seconds, url):
        return WebDriverWait(self.browser, seconds).until(
            EC.url_contains(url))

    def enter_random_text(self, by, locator):
        if self.temporal == None:
            self.temporal = str(time.time())
        self.find_elem(by, locator).send_keys(self.temporal)

    # To challenge myself

    # Exact copy of click_elem, so it's redundant... Maybe there is a better hack exist with out JS.
    def scroll_to_element(self, by, locator):
        self.find_elem(by, locator).click()

    def goto_url(self, url):
        self.browser.get(url)

    def clear_input(self, by, locator):
        self.find_elem(by, locator).clear()

    def replace_input_text(self, by, locator, text):
        element = self.find_elem(by, locator)
        element.clear()
        element.send_keys(text)

    def get_elem_value(self, value, by, locator):
        self.saved_elem_value = self.find_elem(by, locator).get_attribute(value)

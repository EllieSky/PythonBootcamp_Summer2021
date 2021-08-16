from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN


class BaseMethods:

    def __init__(self, browser):
        self.browser: WebDriver = browser
        self.wait: WebDriverWait = WebDriverWait(browser, 5)

    def find_elem(self, by, locator) -> WebElement:
        # return self.browser.find_element(by, locator)
        # return self.wait.until(EC.presence_of_element_located([by, locator]))
        # or
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

    def goto_url(self, url):
        self.browser.get(DOMAIN + url)

    def clear_input(self, by, locator):
        self.find_elem(by, locator).clear()

    def get_elem_value(self, by, locator) -> str:
        return self.browser.find_element(by, locator).get_attribute('value')

    def scroll_to_elem(self, by, locator):
        target = self.find_elem(by, locator)
        ActionChains(self.browser).move_to_element(target).perform()

    def replace_input_text(self, by, locator, text2):
        self.find_elem(by, locator).clear()
        self.find_elem(by, locator).send_keys(text2)

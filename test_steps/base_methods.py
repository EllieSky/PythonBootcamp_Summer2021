from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethods:
    def __init__(self, browser):
        self.browser: WebDriver = browser
        self.wait: WebDriverWait = WebDriverWait(browser, 5)

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
        return WebDriverWait(self.browser, int(seconds)).until(
            EC.visibility_of_element_located((by, locator)))

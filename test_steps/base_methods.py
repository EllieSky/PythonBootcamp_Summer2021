from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from behave import step


class BaseMethods:
    def __init__(self, browser):
        self.browser: WebDriver = browser
        self.wait: WebDriverWait = WebDriverWait(browser, 5)

    @step('I find the element {by}={locator}')
    def find_elem(self, by, locator) -> WebElement:
        # return self.browser.find_element(by, locator)
        # return self.wait.until(EC.presence_of_element_located([by, locator]))
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    @step('I click the element {by}={locator}')
    def click_elem(self, by, locator):
        self.find_elem(by, locator).click()

    @step('I enter text {text} into the element {by}={locator}')
    def enter_text(self, text, by, locator):
        self.find_elem(by, locator).send_keys(text)

    @step('I get the text from element {by}={locator}')
    def get_text(self, by, locator) -> str:
        return self.find_elem(by, locator).text

    @step('I wait for the element {by}={locator} to be visible for {seconds} seconds')
    def wait_for_elem_visible(self, by, locator, seconds):
        return WebDriverWait(self.browser, seconds).until(
            EC.visibility_of_element_located((by, locator)))

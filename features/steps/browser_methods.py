from selenium.webdriver.remote.webelement import WebElement
from behave import step


@step('I find the element {by}={locator}')
def find_elem(context, by, locator) -> WebElement:
    return context.base_methods.find_elem(by, locator)

@step('I click the element {by}={locator}')
def click_elem(context, by, locator):
    context.base_methods.click_elem(by, locator)

@step('I enter text {text} into the element {by}={locator}')
def enter_text(context, text, by, locator):
    context.base_methods.enter_text(text, by, locator)

@step('I get the text from element {by}={locator}')
def get_text(context, by, locator) -> str:
    return context.base_methods.get_text(by, locator)

@step('I wait for the element {by}={locator} to be visible for {seconds} seconds')
def wait_for_elem_visible(context, by, locator, seconds):
    context.base_methods.wait_for_elem_visible(by, locator, seconds)

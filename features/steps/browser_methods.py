import re
from features import vars

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import behave
from behave import step


# @behave.step()
# or
@step('I find the element by {by}={locator}')
def find_elem(context, by, locator) -> WebElement:
    # return context.base_methods.browser.find_element(by, locator)
    # return context.base_methods.wait.until(EC.presence_of_element_located([by, locator]))
    # or
    return context.base_methods.find_elem(by, locator)


@step('I click the element by {by}={locator}')
def click_elem(context, by, locator):
    context.base_methods.click_elem(by, locator)


@step('I enter text {text} into the element by {by}={locator}')
def enter_text(context, text, by, locator):
    context.base_methods.enter_text(_clean(text), by, locator)


@step('I get the text from element by {by}={locator} as {var} variable')
def get_text(context, by, locator, var) -> str:
    setattr(context, var, context.base_methods.get_text(by, locator))


@step('I wait for the element by {by}={locator} to be visible for {seconds} seconds')
def wait_for_elem_visible(context, by, locator, seconds):
    context.base_methods.wait_for_elem_visible(by, locator, seconds)


def _clean(text: str):
    match = re.search(r"\${(.+)}", text)
    if match:
        if getattr(vars, match.group(1), False):
            text = re.sub(r"\${.+}", getattr(vars, match.group(1)), text)  # regular expression regex101.com
    return text if text != 'None' else ''


@step('I go to url {url}')
def goto_url(context, url):
    context.base_methods.goto_url(url)


@step('I clear input by {by}={locator}')
def clear_input(context, by, locator):
    context.base_methods.clear_input(by, locator)


@step('I get element by {by}={locator}')
def get_elem_value(context, by, locator):
    context.base_methods.get_elem_value(by, locator)


@step('I scroll to element by {by}={locator}')
def scroll_to_elem(context, by, locator):
    context.base_methods.scroll_to_elem(by, locator)


@step('I replace input of element by {by}={locator} with text {text2}')
def replace_input_text(context, by, locator, text2):
    context.base_methods.replace_input_text(by, locator, text2)

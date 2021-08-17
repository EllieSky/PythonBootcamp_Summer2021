import re
import time

from features import vars

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
    context.base_methods.enter_text(_clean(text), by, locator)


@step('I enter TEMPORAL RANDOM text into the element {by}={locator}')
def enter_random_text(context, by, locator):
    context.base_methods.enter_random_text(by, locator)


@step('I get the text from element {by}={locator}')
def get_text(context, by, locator) -> str:
    return context.base_methods.get_text(by, locator)


@step('I wait for the element {by}={locator} to be visible for {seconds} seconds')
def wait_for_elem_visible(context, by, locator, seconds):
    context.base_methods.wait_for_elem_visible(by, locator, seconds)


@step('I wait for {seconds} second(s) for URL to contain {url}')
def wait_for_url(context, seconds, url):
    context.base_methods.wait_for_url(seconds, url)


@step('I wait for {seconds} seconds')
def wait_a_little_bit(context, seconds):
    time.sleep(3)


def _clean(text: str):
    match = re.search(r"\${(.+)}", text)
    if match:
        if getattr(vars, match.group(1), False):
            text = re.sub(r"\${.+}", getattr(vars, match.group(1)), text)
    return text if text != 'None' else ''


# To challenge myself
@step('I scroll to element {by}={locator}')
def scroll_to_element(context, by, locator):
    context.base_methods.scroll_to_element(by, locator)


@step('I goto URL {url}')
def goto_url(context, url):
    context.base_methods.goto_url(url)


@step('I clear input in element {by}={locator}')
def clear_input(context, by, locator):
    context.base_methods.clear_input(by, locator)


@step('I replacing input text in element {by}={locator} to text {text}')
def replace_input_text(context, by, locator, text):
    context.base_methods.replace_input_text(by, locator, text)


@step('I get the {value} value from element {by}={locator}')
def get_elem_value(context, value, by, locator):
    context.base_methods.get_elem_value(value, by, locator)

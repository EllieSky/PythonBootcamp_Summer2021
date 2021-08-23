from time import sleep

from behave import then
from behave import step


# Given, When, Then, And, But
# Given = prereqs
# When = test steps
# Then = assertion


@then('I expect the url to contain {url}')
def assert_url_contains(context, url):
    assert url in context.browser.current_url


@then('I expect element {by}={locator} to have text "{text}"')
def assert_elem_text(context, by, locator, text):
    assert text == context.base_methods.get_text(by, locator)


@step('wait for {seconds} second(s) for updating database')
def wait_for_page_update(context, seconds):
    sleep(int(seconds))

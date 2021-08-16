from behave import then


# Given, When, Then, And, But
# Given = prereqs
# When = test step
# Then = assertion

@then('I expect the url to contain {url}')
def assert_url_contains(context, url):
    # print(url)
    # print(context.browser.current_url)
    assert url in context.browser.current_url


@then('I expect element {by}={locator} to have text "{text}"')
def assert_elem_text(context, by, locator, text):
    print(text)
    print(context.base_methods.get_text(by, locator))
    assert text == context.base_methods.get_text(by, locator)


@then('I expect element {by}={locator} to have value "{value}"')
def assert_elem_value(context, by, locator, value):
    assert value == context.base_methods.get_elem_value(by, locator)

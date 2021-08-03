from selenium.webdriver.common.by import By

from tests import ADMIN_USER, DEFAULT_PASSWORD

"""
blah
"""


# TODO blah
def authenticate(browser, username=ADMIN_USER, password=DEFAULT_PASSWORD):
    browser.find_element(By.ID, "txtUsername").send_keys(username)
    browser.find_element(By.ID, "txtPassword").send_keys(password)
    browser.find_element(By.ID, "btnLogin").click()

 # inessa_hw_7  part 2
def calculate_first_letter_in_word(rows):
    array = []
    for cell in rows:
        split_words = (str(cell.text)).split()
        second_word_in_row = split_words[1]
        first_letter = second_word_in_row[0]
        array.append(first_letter)
    return array

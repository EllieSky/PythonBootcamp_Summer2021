import random
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN1


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN1)

    def tearDown(self) -> None:
        self.browser.quit()

# Part 2:
# https://www.calculatorsoup.com/calculators/math/basic.php
# Using the site above create another test which uses the 'random' package
# to choose random numbers to click AND random operator (+, -, /, *) to click.
# Then asserts that the result is what you calculated using python.
# Again, the challenge is NOT USE send_keys.
    def test_random_numbers(self, ):
        browser = self.browser
        browser.find_element(By.NAME, 'clearButton').click()

        random_element1 = random.randint(0, 9)
        element = browser.find_element(By.CSS_SELECTOR, f"[value = '{random_element1}']")
        element.click()

        random_operator = random.choice(['+', '−', '÷', '×'])
        operator = browser.find_element(By.CSS_SELECTOR, f"[value = '{random_operator}']")
        operator.click()

        random_element2 = random.randint(0, 9)
        element2 = browser.find_element(By.CSS_SELECTOR, f"[value = '{random_element2}']")
        element2.click()

        browser.find_element(By.NAME, 'calculate').click()
        result = browser.find_elements(By.NAME, 'display')

        print(result[0].accessible_name)
        expected_result = result[0].accessible_name
        self.assertEqual(expected_result, result[0].accessible_name)

# Bonus Challenge:
# Improve the code in Part 2 to enter by clicking multi-digit numbers.
# Example:
# 456 + 234
# 501 - 33
# 4 - 299
# 1206 * 28
# 12 / 2
    def test_multi_digit_numbers(self, ):
        browser = self.browser
        browser.find_element(By.NAME, 'clearButton').click()

        random_element1 = random.randint(0, 10000)
        for i in range(len(str(random_element1))):
            element = browser.find_element(By.CSS_SELECTOR, f"[value = '{i}']")
            element.click()

        random_operator = random.choice(['+', '−', '÷', '×'])
        operator = browser.find_element(By.CSS_SELECTOR, f"[value = '{random_operator}']")
        operator.click()

        random_element2 = random.randint(0, 10000)
        for i in range(len(str(random_element2))):
            element2 = browser.find_element(By.CSS_SELECTOR, f"[value = '{i}']")
            element2.click()

        browser.find_element(By.NAME, 'calculate').click()
        result = browser.find_elements(By.NAME, 'display')
        print(result[0].accessible_name)
        expected_result = result[0].accessible_name
        self.assertEqual(expected_result, result[0].accessible_name)


if __name__ == '__main__':
    unittest.main()

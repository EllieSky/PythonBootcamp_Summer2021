import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests import CHROME_PATH, DOMAIN1
# Part 1:
# Create a parameterized template with test data for the following site:
# https://www.calculatorsoup.com/calculators/math/basic.php
# tests:
# 1 + 2 = 3
# 4 / 0 = Not a Number
# 4 / 3 = 1.3333333333
# 9 * 5 = 45
# 0 - 4 = -4
# Your test should CLICK the numbers, NOT ENTER them using send_keys

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN1)

    def tearDown(self) -> None:
        self.browser.quit()

    @parameterized.expand([
        ('sum', 'one', 'add', 'two', '3'),
        ('division_by_zero', 'four', 'divide', 'zero', 'Not a Number'),
        ('division', 'four', 'divide', 'three', '1.3333333333'),
        ('multiply', 'nine', 'multiply', 'five', '45'),
        ('subtract', 'zero', 'subtract', 'four', '-4')
    ])
    def test_sum(self, test_name, value1, operator, value2, expected_result):
        browser = self.browser
        browser.find_element(By.NAME, 'clearButton').click()
        browser.find_element(By.NAME, value1).click()
        browser.find_element(By.NAME, operator).click()
        browser.find_element(By.NAME, value2).click()
        browser.find_element(By.NAME, 'calculate').click()
        result = browser.find_elements(By.NAME, 'display')
        print(result[0].accessible_name)
        self.assertEqual(expected_result, result[0].accessible_name)

    # # 1 + 2 = 3
    # def test_sum(self):
    #     self.browser.find_element(By.NAME, 'clearButton').click()
    #     self.browser.find_element(By.NAME, 'one').click()
    #     self.browser.find_element(By.NAME, 'add').click()
    #     self.browser.find_element(By.NAME, 'two').click()
    #     self.browser.find_element(By.NAME, 'calculate').click()
    #     result = self.browser.find_elements(By.NAME, 'display')
    #     print(result[0].accessible_name)
    #     expected_result = '3'
    #     self.assertEqual(expected_result, result[0].accessible_name)
    #
    #     # 4 / 0 = Not a Number
    # def test_error(self):
    #     self.browser.find_element(By.NAME, 'clearButton').click()
    #     self.browser.find_element(By.NAME, 'four').click()
    #     self.browser.find_element(By.NAME, 'divide').click()
    #     self.browser.find_element(By.NAME, 'zero').click()
    #     self.browser.find_element(By.NAME, 'calculate').click()
    #     result = self.browser.find_elements(By.NAME, 'display')
    #     print(result[0].accessible_name)
    #     expected_result = "Not a Number"
    #     self.assertEqual(expected_result, result[0].accessible_name)
    #
    #     # 4 / 3 = 1.3333333333
    # def test_decimal(self):
    #     self.browser.find_element(By.NAME, 'clearButton').click()
    #     self.browser.find_element(By.NAME, 'four').click()
    #     self.browser.find_element(By.NAME, 'divide').click()
    #     self.browser.find_element(By.NAME, 'three').click()
    #     self.browser.find_element(By.NAME, 'calculate').click()
    #     result = self.browser.find_elements(By.NAME, 'display')
    #     print(result[0].accessible_name)
    #     expected_result = '1.3333333333'
    #     self.assertEqual(expected_result, result[0].accessible_name)
    #
    #     # 9 * 5 = 45
    # def test_multiply(self):
    #     self.browser.find_element(By.NAME, 'clearButton').click()
    #     self.browser.find_element(By.NAME, 'nine').click()
    #     self.browser.find_element(By.NAME, 'multiply').click()
    #     self.browser.find_element(By.NAME, 'five').click()
    #     self.browser.find_element(By.NAME, 'calculate').click()
    #     result = self.browser.find_elements(By.NAME, 'display')
    #     print(result[0].accessible_name)
    #     expected_result = '45'
    #     self.assertEqual(expected_result, result[0].accessible_name)
    #
    #     # 0 - 4 = -4
    # def test_subtract(self):
    #         self.browser.find_element(By.NAME, 'clearButton').click()
    #         self.browser.find_element(By.NAME, 'zero').click()
    #         self.browser.find_element(By.NAME, 'subtract').click()
    #         self.browser.find_element(By.NAME, 'four').click()
    #         self.browser.find_element(By.NAME, 'calculate').click()
    #         result = self.browser.find_elements(By.NAME, 'display')
    #         print(result[0].accessible_name)
    #         expected_result = '-4'
    #         self.assertEqual(expected_result, result[0].accessible_name)


if __name__ == '__main__':
    unittest.main()

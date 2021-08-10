import unittest
import operator
from gettext import gettext
from random import random, randrange

from parameterized import parameterized

from selenium import webdriver
from selenium.webdriver.common.by import By

from PythonBootcamp_Summer2021.tests import CHROME_PATH

CALC_DOMAIN = "https://www.calculatorsoup.com/calculators/math/basic.php"


class CalcTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(CALC_DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()



    @parameterized.expand([
        ('Addition', "456", 'add', "234", "690"),
        # TODO VadimG figure the result assertion
        # ('Random addition', randrange(1, 999, 1), 'add', randrange(1, 999, 1), "?????????"),
        ('Subtraction', '501', 'subtract', "34", "467"),
        # Weird but 33 fails as it does not enter second 3 from the iteration and as a result assertion fails
        ('Subtraction', '4', 'subtract', "299", "-295"),
        ('Multiplication', '1206', 'multiply', "28", "33768"),
        ('Division', '12', 'divide', "2", "6"),
        ('Division by zero', '4', 'divide', "0", "Not a Number"),
        ('Fractions', '4', 'divide', "3", "1.3333333333")

    ])

    def test_addition(self, test_name, number1, operation, number2, result):
        input1 = [int(i) for i in str(number1)]
        input2 = [int(i) for i in str(number2)]
        operation = str(operation)
        equals = "="
        for i in input1:
            self.browser.find_element(By.XPATH, "//input[@value='" + str(i) + "']").click()
        self.browser.find_element(By.XPATH, "//input[@name='" + operation + "']").click()
        for i in input2:
            self.browser.find_element(By.XPATH, "//input[@value='" + str(i) + "']").click()
        self.browser.find_element(By.XPATH, "//input[@value='" + equals + "']").click()
        self.assertEquals(result, self.browser.find_element(By.ID, "display").get_attribute("value"))

if __name__ == '__main__':
    unittest.main()

"""
Part 1:
Create a parameterized template with test data for the following site:
https://www.calculatorsoup.com/calculators/math/basic.php
tests:
1 + 2 = 3
4 / 0 = Not a Number
4 / 3 = 1.3333333333
9 * 5 = 45
0 - 4 = -4
Your test should CLICK the numbers, NOT ENTER them using send_keys

Part 2:
Using the site above create another test which uses the 'random' package
to choose random numbers to click AND random operator (+, -, /, *) to click.
Then asserts that the result is what you calculated usig python.
Again, the challenge is NOT USE send_keys.
Bonus Challenge:
Improve the code in Part 2 to enter by clicking multi-digit numbers.
Example:
456 + 234
501 - 33
4 - 299
1206 * 28
12 / 2
"""

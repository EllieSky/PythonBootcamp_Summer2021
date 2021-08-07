import random
import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def expected_result_calculation(digit1, operator: str, digit2) -> str:
    if operator == '+':
        expected_result = str(digit1 + digit2)
    elif operator == '-':
        expected_result = str(digit1 - digit2)
    elif operator == '*':
        expected_result = str(digit1 * digit2)
    elif operator == '/':
        if digit1 == 0:
            expected_result = '0'
        elif digit2 == 0:
            expected_result = 'Not a Number'
        else:
            expected_result = str(round(digit1 / digit2, 10))
            if expected_result[-1] == '0':
                expected_result = expected_result[:-2]
    return expected_result


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # Given url: contains dynamic and changeable ads, which slowing down page loading
        self.browser.get('https://www.calculatorsoup.com/calculators/math/basic.php')
        # Second url option: no ads contains (faster page loading and execution of test cases up to 6 times)
        # self.browser.get('https://www.theonlinecalculator.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    @parameterized.expand([
        ('test1', '1', '+', '2', '3'),
        ('test2', '4', '/', '0', 'Not a Number'),
        ('test3', '4', '/', '3', '1.3333333333'),
        ('test4', '9', '*', '5', '45'),
        ('test5', '0', '-', '4', '-4')
    ])
    def test_calculator_part1_parametrized(self, test_name, first_digit, operator, second_digit, expected_result):
        wd = self.browser
        wd.find_element(By.XPATH, f"//input[@value='{first_digit}']").click()
        wd.find_element(By.XPATH, f"//input[@onclick=\"enterOperator('{operator}')\"]").click()
        wd.find_element(By.XPATH, f"//input[@value='{second_digit}']").click()
        wd.find_element(By.XPATH, "//input[@value='=']").click()
        actual_result = wd.find_element(By.XPATH, "//input[@id='display']").get_dom_attribute('value')
        self.assertEqual(expected_result, actual_result)

    def test_calculator_part2_random_numbers_and_operators(self):
        wd = self.browser
        wait = WebDriverWait(wd, 3)
        operators = ('+', '-', '/', '*')
        first_digit = random.randrange(10)
        operator = random.choice(operators)
        second_digit = random.randrange(10)
        expected_result = expected_result_calculation(first_digit, operator, second_digit)
        wd.find_element(By.XPATH, f"//input[@value='{first_digit}']").click()
        wait.until(expected_conditions.text_to_be_present_in_element_value(
            (By.XPATH, "//input[@id='display']"), str(first_digit)))
        wd.find_element(By.XPATH, f"//input[@onclick=\"enterOperator('{operator}')\"]").click()
        wd.find_element(By.XPATH, f"//input[@value='{second_digit}']").click()
        wait.until(expected_conditions.text_to_be_present_in_element_value(
            (By.XPATH, "//input[@id='display']"), str(second_digit)))
        wd.find_element(By.XPATH, "//input[@value='=']").click()
        actual_result = wd.find_element(By.XPATH, "//input[@id='display']").get_dom_attribute('value')
        print(f'{first_digit} {operator} {second_digit}')
        print(f"expected = {expected_result}")
        print(f"actual = {actual_result}")
        self.assertEqual(expected_result, actual_result)

    def test_calculator_part3_random__multi_digits_numbers_and_operators(self):
        wd = self.browser
        wait = WebDriverWait(wd, 30)
        operators = ('+', '-', '/', '*')
        first_digit = random.randrange(1000000)
        operator = random.choice(operators)
        second_digit = random.randrange(1000000)
        expected_result = expected_result_calculation(first_digit, operator, second_digit)
        for x in range(len(str(first_digit))):
            wd.find_element(By.XPATH, f"//input[@value='{str(first_digit)[x]}']").click()
        wait.until(expected_conditions.text_to_be_present_in_element_value(
            (By.XPATH, "//input[@id='display']"), str(first_digit)))
        wd.find_element(By.XPATH, f"//input[@onclick=\"enterOperator('{operator}')\"]").click()
        for x in range(len(str(second_digit))):
            wd.find_element(By.XPATH, f"//input[@value='{str(second_digit)[x]}']").click()
        wait.until(expected_conditions.text_to_be_present_in_element_value(
            (By.XPATH, "//input[@id='display']"), str(second_digit)))
        wd.find_element(By.XPATH, "//input[@value='=']").click()
        actual_result = wd.find_element(By.XPATH, "//input[@id='display']").get_dom_attribute('value')
        print(f'{first_digit} {operator} {second_digit}')
        print(f"expected = {expected_result}")
        print(f"actual = {actual_result}")
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()

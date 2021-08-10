import random
import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH


class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.driver.get("https://www.calculatorsoup.com/calculators/math/basic.php")

        wait = WebDriverWait(self.driver, 5, 0.2)
        wait.until(EC.presence_of_element_located((By.ID, "display")))

    def tearDown(self) -> None:
        self.driver.quit()

    @parameterized.expand([
        ("addition", 1, 2, "+", 3),
        ("division false", 4, 0, "÷", "Not a Number"),
        ("division", 4, 3, "÷", 1.3333333333),
        ("multiplication", 9, 5, "×", 45),
        ("subtraction", 0, 4, "−", -4)
    ])
    def test_hw_part1_parameterized(self, _, input1, input2, operator, result):
        self.driver.find_element(By.CSS_SELECTOR, 'input.button.number[value="{}"]'.format(input1)).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input.button.operator[value="{}"]'.format(operator)).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input.button.number[value="{}"]'.format(input2)).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input.button.operator[value="="]').click()
        actual_result = self.driver.find_element(By.ID, "display").get_attribute('value')
        # sleep(4)
        self.assertEqual(str(result), actual_result)

    def test_hw_part2_random_bonus(self):
        input1 = random.randint(0, 999)
        input2 = random.randint(0, 999)
        operators_pairs = [["+", "+"], ["−", "-"], ["×", "*"], ["÷", "/"]]
        operator_index = random.randint(0, 3)

        for digit in str(input1):
            self.driver.find_element(By.CSS_SELECTOR, 'input.button.number[value="{}"]'.format(digit)).click()

        self.driver.find_element(By.CSS_SELECTOR, 'input.button.operator[value="{}"]'.format(operators_pairs[operator_index][0])).click()

        for digit in str(input2):
            self.driver.find_element(By.CSS_SELECTOR, 'input.button.number[value="{}"]'.format(digit)).click()

        self.driver.find_element(By.CSS_SELECTOR, 'input.button.operator[value="="]').click()

        actual_result = self.driver.find_element(By.ID, "display").get_attribute('value')
        string_for_calculation = str(input1) + operators_pairs[operator_index][1] + str(input2)
        calculated_result = eval(string_for_calculation)

        # print("string_for_calculation: ", string_for_calculation)
        # print("calculated_result: ", calculated_result)
        # print("actual_result: ", actual_result)
        self.assertEqual(str(calculated_result), actual_result)


if __name__ == '__main__':
    unittest.main()

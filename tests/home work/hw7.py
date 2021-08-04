import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authentification
from tests import DOMAIN, CHROME_PATH, ADMIN_USER, DEFAULT_PASSWORD


class TestsHomeWork7(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    # Part 1: Negative tests for login page functionality
    def test_blank_username_and_blank_password(self):
        wb = self.browser
        expected = "Username cannot be empty"
        wb.find_element(By.ID, "btnLogin").click()
        actual = wb.find_element(By.XPATH, "//div/span[@id='spanMessage']").text
        self.assertEqual(expected, actual)

    def test_valid_username_and_invalid_password(self):
        wb = self.browser
        expected = "Password cannot be empty"
        wb.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        wb.find_element(By.ID, "btnLogin").click()
        actual = wb.find_element(By.XPATH, "//div/span[@id='spanMessage']").text
        self.assertEqual(expected, actual)

    def test_invalid_username_and_valid_password(self):
        wb = self.browser
        expected = "Username cannot be empty"
        wb.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        wb.find_element(By.ID, "btnLogin").click()
        actual = wb.find_element(By.XPATH, "//div/span[@id='spanMessage']").text
        self.assertEqual(expected, actual)

    # Part 2: Test for sorting table values by First (Middle) Name column
    def test_sorting_table_values(self):
        wb = self.browser
        authentification(wb)
        WebDriverWait(self.browser, 5).until(expected_conditions.url_contains("/pim/viewEmployeeList"))
        wb.find_element(By.XPATH, "//thead/tr/th[3]/a").click()
        WebDriverWait(self.browser, 5).until(expected_conditions.url_contains(
            "viewEmployeeList?sortField=firstMiddleName&sortOrder=ASC"))
        actual_list_of_web_elements = wb.find_elements(By.XPATH, "//tbody/tr/td[3]/a")
        actual_list = []
        for x in actual_list_of_web_elements:
            actual_list.append(x.text)
        sorted_list = sorted(actual_list)
        self.assertEqual(sorted(actual_list), actual_list)

    # Part 3: Bonus challenge
    # Sorting table values by First (Middle) Name column
    # for all pages of employee records
    def test_table_value_for_all_pages(self):
        wb = self.browser
        authentification(wb)
        WebDriverWait(self.browser, 5).until(expected_conditions.url_contains("/pim/viewEmployeeList"))
        wb.find_element(By.XPATH, "//thead/tr/th[3]/a").click()
        WebDriverWait(self.browser, 5).until(expected_conditions.url_contains(
            "viewEmployeeList?sortField=firstMiddleName&sortOrder=ASC"))
        # page_count = int(wb.find_element(By.XPATH, "//div[@class='top']/ul/li[1]").text.split()[-1])
        # for x in range(int(page_count / 50) + 1):
        #     if x > 0:
        #         wb.find_element(By.XPATH, "//div[@class='top']/ul/li[6]/a").click()
        #     actual_list_of_web_elements = wb.find_elements(By.XPATH, "//tbody/tr/td[3]/a")
        #     actual_list = []
        #     for value in actual_list_of_web_elements:
        #         actual_list.append(value.text)
        #     # sorted_list = sorted(actual_list)
        #     self.assertEqual(sorted(actual_list), actual_list)
        # Second way (still checking all data pages in table)
        # while True:
        #     actual_list_of_web_elements = wb.find_elements(By.XPATH, "//tbody/tr/td[3]/a")
        #     actual_list = []
        #     for value in actual_list_of_web_elements:
        #         actual_list.append(value.text)
        #     self.assertEqual(sorted(actual_list), actual_list)
        #     if len(actual_list) == 50:
        #         wb.find_element(By.XPATH, "//div[@class='top']/ul/li[6]/a").click()
        #     else:
        #         return False
        # Third way (same logic that in 'Second way', but we checking only first and last table data page)
        while True:
            actual_list_of_web_elements = wb.find_elements(By.XPATH, "//tbody/tr/td[3]/a")
            actual_list = []
            for value in actual_list_of_web_elements:
                actual_list.append(value.text)
            self.assertEqual(sorted(actual_list), actual_list)
            if len(actual_list) == 50:
                wb.find_element(By.XPATH, "//div[@class='top']/ul/li[7]/a").click()
            else:
                return False


if __name__ == '__main__':
    unittest.main()

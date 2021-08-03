import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN

# Part 2:
# Using the site above create a test for sorting table values by First (Middle) Name column
# 1. Login  (admin/password)
# 2. Scroll down to the Employee list table
# 3. Click the "First (Middle) Name" table header
# 4. Wait for the sort to complete (hint: url)
# 5. Ensure the records on the first page are listed in alphabetical order by name
# Bonus Challenge:
# Extend the test above to include all pages of employee records
# Assume there can be more then the current number of pages and you don't know how many there will be eventually.
from time import sleep
from unittest import skip


class SortingFirstName(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("pim/viewEmployeeList"))

    def tearDown(self) -> None:
        self.browser.quit()

    def test_sorting_first_name(self):
        self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/thead/tr/th[3]/a').click()
        sorted_column_first_name = self.browser.find_elements(By.XPATH, '//tr//td[3]')

        column_ls = []
        for name in sorted_column_first_name:
            # print(name.text)
            column_ls.append(name.text)
        print(column_ls)

        sorted_ls = []
        for name in sorted_column_first_name:
            # print(name.text)
            sorted_ls.append(name.text)
        sorted_ls = sorted(sorted_ls)
        print(sorted_ls)

        self.assertTrue(sorted_ls == column_ls)



if __name__ == '__main__':
    unittest.main()

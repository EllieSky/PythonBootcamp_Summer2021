import math
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class TableSortTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_pim_table_first_name_sort(self):
        browser = self.browser
        wait = WebDriverWait(browser, 5)

        wait.until(expected_conditions.presence_of_element_located(
            [By.LINK_TEXT, "First (& Middle) Name"])).click()

        wait.until(expected_conditions.url_contains("sortOrder=ASC"))
        # OR (you do not need both)
        wait.until(expected_conditions.element_attribute_to_include(
            [By.LINK_TEXT, "First (& Middle) Name"], 'class'
        )) #TODO: look up usage syntax

        list_of_first_name_elms = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]')

        has_pagination = browser.find_elements(By.CLASS_NAME, 'desc')
        pages = 1
        if has_pagination:
            records = int(has_pagination[0].text.split()[-1])
            pages = math.ceil(records / 50)

        previous = ''

        for page in range(1, pages+1):
            for name_elm in list_of_first_name_elms:
                current = name_elm.text
                self.assertGreaterEqual(current, previous,
                                        f"Expected name '{current}' to be after '{previous}', but it was not")
                print(f"Name '{current}' was after '{previous}'")
                previous = current

            if page < pages:
                browser.find_element(By.LINK_TEXT, "Next").click()
                list_of_first_name_elms = browser.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]')






if __name__ == '__main__':
    unittest.main()

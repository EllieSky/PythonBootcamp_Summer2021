import math
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from steps.common import authenticate
from PythonBootcamp_Summer2021.tests import CHROME_PATH, DOMAIN


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_pim_table_name_sort(self)
        browser = self.browser
        wait = WebDriverWait(browser, 5)


        wait.until(expected_conditions.presence_of_element_located(
            [By.LINK_TEXT, "First (& Middle) Name"])).click()


        wait.until(expected_conditions.url_contains("sortOrder=ASC"))
        [By.LINK_TEXT, "First (& Middle) Name], 'class'


        list_of_first_name_elms = browser.find.elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr/td[3]')

        previous = ''
        for name_elm in list_of_first_name_elms:
            current = name_elm.text
            self.assertGreaterEqual(name_elm.text, previous,
                                    f"Expected name '{name_elm.text}' to be after '{previous}, but it was not")

            #print(f"Name {current} after '{previous}'")
            previous = current

        has_pagination = browser.find_element(By.CLASS_NAME, 'desc')
        if has_pagination:
            record = int(has_pagination[0].text.split()[-1])
            math.ceil(records /50)

        previous = ''

        for page in range

if __name__ == '__main__':
    unittest.main()

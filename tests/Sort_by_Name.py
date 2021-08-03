import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonBootcamp_Summer2021.steps.common import authenticate
from PythonBootcamp_Summer2021.tests import CHROME_PATH, DOMAIN

"""
Using the site above create a test for sorting table values by First (Middle) Name column
1. Login  (admin/password) - DONE 
2. Scroll down to the Employee list table - DONE
3. Click the "First (Middle) Name" table header - DONE
4. Wait for the sort to complete (hint: url) - DONE
5. Ensure the records on the first page are listed in alphabetical order by name
"""

class SortByNameTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)


    def test_sortByName(self):
        self.browser.find_element(By.LINK_TEXT, "First (& Middle) Name").click()
        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("sortField=firstMiddleName&sortOrder="))
    #   Validation of "sortField=firstMiddleName&sortOrder=" should include "ASC" as well as "DESC"
        self.assertIn("A", self.browser.find_element(By.XPATH, "// *[ @ id = 'resultTable'] / tbody / tr[1] / td[3]").text)
    #   Validation is not totally correct as we assume that the first entry starts with "A", validation failes if there are no names that starts with "A"




    def tearDown(self) -> None:
        self.browser.quit()
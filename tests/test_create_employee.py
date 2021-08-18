import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from test_steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class CreateEmployeeTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

    def tearDown(self) -> None:
        self.browser.quit()


    # TODO: DEBUG and convert to POM
    # NOTE: this needs explicit wait added at several point in the code
    def test_create_employee_no_creds(self):
        browser = self.browser

        emp_id = str(int(time.time() * 1000))[4:]

        browser.find_element(By.ID, "btnAdd").click()

        self.assertEqual("Add Employee", browser.find_element(By.TAG_NAME, "h1").text)

        browser.find_element(By.ID, "firstName").send_keys('Steve')
        browser.find_element(By.ID, "lastName").send_keys('Jones')

        browser.find_element(By.ID, "employeeId").clear()
        browser.find_element(By.ID, "employeeId").send_keys(emp_id)

        browser.find_element(By.ID, "btnSave").click()

        self.assertEqual("Personal Details", browser.find_element(By.CSS_SELECTOR, ".personalDetails h1").text)

        self.browser.find_element(By.XPATH, '//*[@id="sidenav"]//a[text()="Job"]').click()
        # Edit button
        browser.find_element(By.ID, "btnSave").click()

        Select(browser.find_element(By.ID, "job_sub_unit")).select_by_visible_text("HR")
        browser.find_element(By.ID, "btnSave").click()  # Save button

        browser.find_element(By.LINK_TEXT, "PIM").click()
        self.browser.find_element(By.ID, 'empsearch_id').send_keys(emp_id)
        self.browser.find_element(By.ID, 'searchBtn').click()

        rows = self.browser.find_elements(By.XPATH, "//tbody/tr")
        self.assertEqual(1, len(rows))

        self.assertEqual(emp_id, self.browser.find_element(By.XPATH, '//tbody/tr/td[2]/a').text)
        self.assertEqual('Steve', self.browser.find_element(By.XPATH, '//tbody/tr/td[3]/a').text)
        self.assertEqual('Jones', self.browser.find_element(By.XPATH, '//tbody/tr/td[4]/a').text)
        self.assertEqual('HR', self.browser.find_element(By.XPATH, '//tbody/tr/td[7]').text)



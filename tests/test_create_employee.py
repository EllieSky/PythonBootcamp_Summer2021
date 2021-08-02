import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenticate
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

    # TODO: WORK IN PROGRESS
    def test_create_employee_no_creds(self):
        browser = self.browser

        emp_id = str(int(time.time() * 1000))[4:]

        browser.find_element(By.ID, "btnAdd").click()
        self.assertEqual("Add Employee", browser.find_element(By.TAG_NAME, "h1").text)

        browser.find_element(By.ID, "firstName").send_keys('Test')
        browser.find_element(By.ID, "lastName").send_keys('Employee')

        browser.find_element(By.ID, "employeeId").clear()
        browser.find_element(By.ID, "employeeId").send_keys(emp_id)

        browser.find_element(By.ID, "btnSave").click()

        self.assertEqual("Personal Details", browser.find_element(By.CSS_SELECTOR, ".personalDetails h1").text)

        # Edit button
        browser.find_element(By.ID, "btnSave").click()

        browser.find_element(By.ID, "personal_optGender_1").click()
        browser.find_element(By.ID, "btnSave").click()  # Save button

        browser.find_element(By.LINK_TEXT, "PIM").click()

    def test_validate_employee_list_sorting_rules(self):
        browser = self.browser
        wait = WebDriverWait(browser, 5)

        # Step 1: Open Employee List page
        browser.find_element(By.ID, "menu_pim_viewEmployeeList").click()
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))
        self.assertEqual("Employee List", browser.find_element(By.CLASS_NAME, "selected").text)

        # Step 2: Scroll down to the Employee list table
        browser.find_element(By.ID, 'footer').location_once_scrolled_into_view

        # Step 3. Click the "First (Middle) Name" table header
        browser.find_element(By.LINK_TEXT, "First (& Middle) Name").click()

        # 4. Wait for the sort to complete (hint: url)
        wait.until(expected_conditions.url_contains("ASC"))
        url_partial = browser.current_url.split("?")
        self.assertEqual("sortField=firstMiddleName&sortOrder=ASC", url_partial[1])

        # 5. Ensure the records on the first page listed in alphabetical order by name
        rows = browser.find_elements(By.XPATH, "//tbody/tr")
        list_of_names = []

        for single_row in rows:
            list_of_names.append(single_row.find_element(By.XPATH, ".//td[3]").text)

        print(list_of_names)
        self.assertEqual(sorted(list_of_names), list_of_names)

        # Bonus Challenge
        form = browser.find_element(By.ID, "frmList_ohrmListComponent")
        pages = form.find_elements(By.XPATH, "//div[1]/ul")

        list_all_names = []
        for page in pages:
            rows = browser.find_elements(By.XPATH, "//tbody/tr")
            for single_row in rows:
                list_all_names.append(single_row.find_element(By.XPATH, ".//td[3]").text)
            if browser.find_element(By.LINK_TEXT, "Next"):
                browser.find_element(By.LINK_TEXT, "Next").click()
        print(list_all_names)
        self.assertEqual(sorted(list_all_names), list_all_names)


if __name__ == '__main__':
    unittest.main()
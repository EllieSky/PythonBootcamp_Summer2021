<<<<<<< Updated upstream
import time
=======
>>>>>>> Stashed changes
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
<<<<<<< Updated upstream
from selenium.webdriver.support.wait import WebDriverWait

=======
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from homework_inessa import ID_VALUE
>>>>>>> Stashed changes
from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


<<<<<<< Updated upstream
class CreateEmployeeTests(unittest.TestCase):
=======
class MyTestCase(unittest.TestCase):
>>>>>>> Stashed changes
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

    def tearDown(self) -> None:
        self.browser.quit()

<<<<<<< Updated upstream

    # TODO: WORK IN PROGRESS
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

        # Edit button
        browser.find_element(By.ID, "btnSave").click()

        browser.find_element(By.ID, "personal_optGender_1").click()
        browser.find_element(By.ID, "btnSave").click()  # Save button

        browser.find_element(By.LINK_TEXT, "PIM").click()
        pass

=======
    def test_create_employee_no_creds(self):
      browser = self.browser
      browser.find_element(By.ID, "btnAdd").click()
      self.assertEqual("Add Employee", browser.find_element(By.TAG_NAME, "h1").text)
      browser.find_element(By.ID, "firstName").send_keys('Ellen')
      browser.find_element(By.ID, "lastName").send_keys('Ford')
      browser.find_element(By.ID, "employeeId").clear()
      browser.find_element(By.ID, "employeeId").send_keys('saasadasdqè234324')
      browser.find_element(By.ID, "btnSave").click()
      browser.find_element(By.ID, "btnSave").click()
      browser.find_element(By.CSS_SELECTOR, ".personalDetails h1").text
      browser.find_element(By.ID, "btnSave").click()



if __name__ == '__main__':
    unittest.main()
>>>>>>> Stashed changes

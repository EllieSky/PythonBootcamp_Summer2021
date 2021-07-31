import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authentification
from tests import CHROME_PATH, DOMAIN


class CreateEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authentification(self.browser)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

    def tearDown(self) -> None:
        self.browser.quit()

    def test_create_employee_no_creds(self):
        br = self.browser

        emp_id = str(int(time.time() * 1000))[-5:]

        br.find_element(By.ID, "btnAdd").click()

        self.assertEqual('Add Employee', br.find_element(By.TAG_NAME, 'h1').text)

        br.find_element(By.ID, 'firstName').send_keys("Bob")
        br.find_element(By.ID, 'lastName').send_keys("Ben")

        br.find_element(By.ID, 'employeeId').clear()
        br.find_element(By.ID, 'employeeId').send_keys(emp_id)

        br.find_element(By.ID, 'btnSave').click()

        self.assertEqual("Personal Details", br.find_element(By.CSS_SELECTOR, '.personalDetails h1').text)

        br.find_element(By.ID, 'btnSave').click()

        br.find_element(By.ID, 'personal_optGender_1').click()
        br.find_element(By.ID, 'btnSave').click()

        br.find_element(By.LINK_TEXT, "PIM").click()
        pass



if __name__ == '__main__':
    unittest.main()

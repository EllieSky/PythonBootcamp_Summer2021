import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


def login_test(self):
    self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
    self.browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
    self.browser.find_element(By.ID, "btnLogin").click()

    wait = WebDriverWait(self.browser, 7)
    wait.until(expected_conditions.url_contains("pim/viewEmployeeList"))


class VerifyEmployeesTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_verify_id_employee_information(self):
        login_test(self)
        self.browser.find_element(By.ID, "empsearch_id").send_keys("0001")
        self.browser.find_element(By.ID, "searchBtn").click()

        expected = self.browser.find_element(By.ID, "empsearch_id").get_attribute("value")
        actual = self.browser.find_element(By.XPATH, "//a[contains(text(),'0001')]").text
        self.assertEqual(expected, actual)
        self.assertEqual("Bob", self.browser.find_element(By.XPATH, "//a[contains(text(),'Bob')]").text)
        self.assertEqual("Boss", self.browser.find_element(By.XPATH, "//a[contains(text(),'Boss')]").text)

    def test_verify_QA_managers_list(self):
        login_test(self)
        self.browser.find_element(By.ID, "empsearch_job_title").click()
        self.browser.find_element(By.XPATH, "//select[@id='empsearch_job_title']/option[@value='38']").click()
        self.browser.find_element(By.ID, "searchBtn").click()

        list_qa_managers = self.browser.find_elements(By.XPATH, "//tr[@class]")
        for qa_manager in list_qa_managers:
            self.assertIn("QA Manager", qa_manager.text)


if __name__ == '__main__':
    unittest.main()

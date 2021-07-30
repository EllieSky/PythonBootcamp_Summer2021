import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authentification
from tests import CHROME_PATH, DOMAIN


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authentification(self.browser)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))


    def tearDown(self) -> None:
        self.browser.quit()

    # Search by employee id for 0001
    def test_part_1(self):

        self.browser.find_element(By.XPATH, "//*[@id='empsearch_id']").send_keys("0001")
        self.browser.find_element(By.XPATH, "//*[@id='searchBtn']").click()

        expected_record_count = 1
        actual_record_count = len(self.browser.find_elements(By.XPATH, "//tbody/tr"))
        self.assertTrue(expected_record_count, actual_record_count)

        expected_raw_value = "0001"
        actual_raw_value = self.browser.find_element(By.XPATH, "//tbody/tr/td[2]/a").text
        self.assertTrue(expected_raw_value == actual_raw_value)

        expected_record = "Bob Boss - QA Manager"
        actual_record = self.browser.find_element(By.XPATH, "//tbody/tr/td[3]/a").text + " " + \
                        self.browser.find_element(By.XPATH, "//tbody/tr/td[4]/a").text + " - " + \
                        self.browser.find_element(By.XPATH, "//tbody/tr//td[5]").text
        self.assertEquals(expected_record, actual_record)

    # Bonus task
    def test_part2(self):
        authentification(self.browser)
        self.browser.find_element(By.XPATH, "//select[@id='empsearch_job_title']").send_keys("QA Manager")
        self.browser.find_element(By.XPATH, "//*[@id='searchBtn']").click()

        actual_data_result = True
        expected_result_record = "QA Manager"
        list_employee = self.browser.find_elements(By.XPATH, "//tbody/tr/td[5]")
        for x in list_employee:
            if x.text != expected_result_record:
                actual_data_result = False
        self.assertTrue(actual_data_result)


if __name__ == '__main__':
    unittest.main()

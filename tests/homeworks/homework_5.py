import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_by_id(self):
        original_url = self.browser.current_url
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        new_url = self.browser.current_url
        self.assertNotEqual(original_url, new_url)

        # HOMEWORK PART

        self.browser.find_element(By.XPATH, "//li[./label[contains(text(), 'Id')]]"
                                            "/input[@type = 'text']").send_keys('0001')

        self.browser.find_element(By.XPATH, "//input[@type = 'button'][@value = 'Search']").click()

        number_of_results = len(self.browser.find_elements(By.XPATH, "//tbody/tr"))
        self.assertEqual(1, number_of_results)

        id_in_results = self.browser.find_element(By.XPATH, "//td/a[contains(text(), '0001')]").text
        self.assertEqual("0001", id_in_results)

        first_name = self.browser.find_element(By.XPATH, "//td/a[text() = 'Bob']").text
        last_name = self.browser.find_element(By.XPATH, "//td/a[text() = 'Boss']").text
        job_title = self.browser.find_element(By.XPATH, "//td[text() = 'QA Manager']").text
        self.assertEqual("Bob", first_name)
        self.assertEqual("Boss", last_name)
        self.assertEqual("QA Manager", job_title)

        # BONUS TASK

        self.browser.find_element(By.XPATH, "//li[./label[contains(text(), 'Id')]]"
                                            "/input[@type = 'text']").clear()

        # selecting QA Manager from dropdown
        job_title_dropdown = self.browser.find_element(By.XPATH, "//select[@id = 'empsearch_job_title']"
                                                                 "/option[text() = 'QA Manager']").click()

        self.browser.find_element(By.XPATH, "//input[@type = 'button'][@value = 'Search']").click()

        # returns a list of job titles from the table

        job_title_to_verify = self.browser.find_elements(By.XPATH, "//tbody//td[contains(text(), 'QA Manager')]")

        # comparing that all items for 'job title' column are 'qa manager' and print them to be sure.

        for item in job_title_to_verify:
            self.assertEqual("QA Manager", item.text)
            print(item.text)


if __name__ == '__main__':
    unittest.main()
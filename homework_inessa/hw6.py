import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework_inessa import ID_VALUE
from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class LoginPageTests(unittest.TestCase):
    # browser variable shared across all tests incide specific class. class
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    #cleanup after test
    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        original_url = self.browser.current_url
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        # wait = WebDriverWait(self.browser, 7)
        # wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))
        #
        # new_url = self.browser.current_url
        # self.assertNotEqual(original_url, new_url)
        #
        # welcome_message = self.browser.find_element(By.ID, "welcome").text
        # self.assertEqual("Welcome Admin", welcome_message)
        #
        # self.browser.find_element(By.TAG_NAME, "h1").text
        # self.assertEqual("Employee Information", self.browser.find_element(By.TAG_NAME, "h1").text)

        self.browser.find_element(By.ID, "empsearch_id").send_keys(ID_VALUE)
        self.browser.find_element(By.ID, "searchBtn").click()
        # correct record
        rows = self.browser.find_element(By.XPATH, "//*[@id='resultTable']/tbody/tr/td[2]").text
        self.assertEqual("0001", rows)

        total_rows = self.browser.find_element(By.XPATH, "//*[@id='resultTable']/tbody/tr")
        z=total_rows.find_element(By.TAG_NAME, "tr")

        x = 0
        for i in z:
            # x += 1
         print(z)





if __name__ == '__main__':
    unittest.main()

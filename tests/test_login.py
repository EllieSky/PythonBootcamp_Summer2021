import unittest
from idlelib import browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenticate, calculate_first_letter_in_word
from tests import CHROME_PATH, DOMAIN


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
        authenticate(self.browser)

        # wait = WebDriverWait(self.browser, 7)
        # wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        new_url = self.browser.current_url
        self.assertNotEqual(original_url, new_url)
        #
        # welcome_message = self.browser.find_element(By.ID, "welcome").text
        # self.assertEqual("Welcome Admin", welcome_message)
        #
        # self.browser.find_element(By.TAG_NAME, "h1").text
        # self.assertEqual("Employee Information", self.browser.find_element(By.TAG_NAME, "h1").text)



    #
    # def test_log_out(self):
    #         pass


    # inessa_hw_7  part 1
    def test_invalid_password(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("admin")
        self.browser.find_element(By.ID, "txtPassword").send_keys("asasxsasaw")
        self.browser.find_element(By.ID, "btnLogin").click()
        result = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]')
        self.assertEqual("Invalid credentials", result.text)


    def test_empty_password(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("admin")
        self.browser.find_element(By.ID, "txtPassword").send_keys("")
        self.browser.find_element(By.ID, "btnLogin").click()
        result = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]')
        self.assertEqual("Password cannot be empty", result.text)

    def test_empty_username(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("")
        self.browser.find_element(By.ID, "txtPassword").send_keys("password")
        self.browser.find_element(By.ID, "btnLogin").click()
        result = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]')
        self.assertEqual("Username cannot be empty", result.text)

    def test_invalid_username(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("kbb")
        self.browser.find_element(By.ID, "txtPassword").send_keys("password")
        self.browser.find_element(By.ID, "btnLogin").click()
        result = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]')
        self.assertEqual("Invalid credentials", result.text)

    def test_username_and_password_empty(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("")
        self.browser.find_element(By.ID, "txtPassword").send_keys("")
        self.browser.find_element(By.ID, "btnLogin").click()
        result = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]')
        self.assertEqual("Username cannot be empty", result.text)

    def test_username_and_password_invalid(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys("dww")
        self.browser.find_element(By.ID, "txtPassword").send_keys("dwwedwd")
        self.browser.find_element(By.ID, "btnLogin").click()
        result = self.browser.find_element(By.XPATH, '//*[@id="spanMessage"]')
        self.assertEqual("Invalid credentials", result.text)

    # inessa_hw_7  part 2
    def test_sorting_values(self):
        authenticate(self.browser)
        self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/thead/tr/th[3]').click()
        wait = WebDriverWait(self.browser, 2)
        rows = self.browser.find_elements(By.XPATH, "//tbody/tr")
        expected_result = sorted(calculate_first_letter_in_word(rows))
        actual_result = calculate_first_letter_in_word(rows)
        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenicate
from tests import CHROME_PATH, DOMAIN


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        original_url = self.browser.current_url
        authenicate(self.browser)

        link_text = self.browser.find_elements(By.LINK_TEXT, "Welcome Admin")
        self.assertTrue(link_text)

        new_url = self.browser.current_url
        self.assertNotEqual(new_url, original_url)

        tag_name_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Employee Information", tag_name_text)

    def test_invalid_login_no_password(self):
        authenicate(self.browser, "admin", None)
        self.assertEqual("Password cannot be empty", self.browser.find_element(By.ID, "spanMessage").text)

    def test_invalid_login_no_username(self):
        authenicate(self.browser, None)
        self.assertEqual("Username cannot be empty", self.browser.find_element(By.ID, "spanMessage").text)

    def test_invalid_login_wrong_password(self):
        authenicate(self.browser, "admin", "Password")
        self.assertEqual("Invalid credentials", self.browser.find_element(By.ID, "spanMessage").text)

    # Expected to fail. No cAsE sensitivity in username field?
    @unittest.expectedFailure
    def test_invalid_login_wrong_username_case_senistivity(self):
        authenicate(self.browser, "Admin")
        self.assertEqual("Invalid credentials", self.browser.find_element(By.ID, "spanMessage").text)

    def test_invalid_login_wrong_username(self):
        authenicate(self.browser, "user")
        self.assertEqual("Invalid credentials", self.browser.find_element(By.ID, "spanMessage").text)

    def test_table_sorting(self):
        authenicate(self.browser)
        all_names = []
        total_names = 0

        wait = WebDriverWait(self.browser, 2, 0.2)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))
        wait.until(expected_conditions.presence_of_element_located((By.ID, "resultTable")))

        self.browser.find_element(By.LINK_TEXT, "First (& Middle) Name").click()
        wait.until(expected_conditions.presence_of_element_located((By.ID, "resultTable")))

        self.assertTrue(self.browser.find_element(By.CLASS_NAME, 'left'))

        if len(self.browser.find_elements(By.CLASS_NAME, "paging")) > 0:
            total_names = int(self.browser.find_element(By.CSS_SELECTOR, "li.desc").text.split()[-1])

            while True:
                for item in self.browser.find_elements(By.XPATH, '//tbody/tr/td[3]'):
                    all_names.append(item.text)

                paging_top = self.browser.find_element(By.CLASS_NAME, "paging.top")
                clean_current_page = int(paging_top.find_element(By.CLASS_NAME, "current").text)

                next_page = self.browser.find_element(By.LINK_TEXT, "Next")
                next_page_href = next_page.get_attribute("href")
                clean_next_page = int(next_page_href.split("(")[1].split(")")[0])

                last_page = self.browser.find_element(By.LINK_TEXT, "Last")
                last_page_href = last_page.get_attribute("href")
                clean_last_page = int(last_page_href.split("(")[1].split(")")[0])

                if clean_current_page == clean_next_page == clean_last_page:
                    break
                else:
                    next_page.click()
                    wait.until(expected_conditions.presence_of_element_located((By.ID, "resultTable")))
        else:
            for item in self.browser.find_elements(By.XPATH, '//tbody/tr/td[3]'):
                all_names.append(item.text)

        self.assertEqual(total_names, len(all_names))
        self.assertEqual(all_names, sorted(all_names))

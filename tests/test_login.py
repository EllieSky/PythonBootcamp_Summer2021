import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from tests import CHROME_PATH, DOMAIN, ADMIN_USER


class LoginPageTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)


if __name__ == '__main__':
    unittest.main()

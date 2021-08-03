import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("pim/viewEmployeeList"))

    def tearDown(self) -> None:
        self.browser.quit()

    def test_logout_test(self):
        self.browser.find_element(By.ID, 'welcome').click()

        logout = self.browser.find_element(By.XPATH, '//*[@id="welcome-menu"]/ul/li[2]/a')
        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.element_to_be_clickable(logout))
        logout.click()

        self.assertIn('LOGIN Panel', self.browser.find_element(By.ID, 'logInPanelHeading').text)


if __name__ == '__main__':
    unittest.main()

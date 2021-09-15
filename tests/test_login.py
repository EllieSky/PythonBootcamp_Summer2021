import os
import csv
import unittest
from typing import List

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from fixtures import BaseFixture
from test_steps.common import authenticate
from tests import DOMAIN, PROJ_HOME


def read_csv(header=True) -> List:
    with open(os.path.join(PROJ_HOME, 'data', 'login_data.csv')) as file:
        reader = csv.reader(file)
        if header:
            next(reader)  # only needed if CSV has headers
        return list(map(tuple, reader))


class LoginPageTests(BaseFixture):
    @unittest.skip
    def test_valid_login(self):
        original_url = self.browser.current_url
        authenticate(self.browser)

        self.wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        new_url = self.browser.current_url
        self.assertNotEqual(original_url, new_url)

        welcome_message = self.browser.find_element(By.ID, "welcome").text
        self.assertEqual("Welcome Admin", welcome_message)

        self.assertEqual("Employee Information",
                         self.browser.find_element(By.TAG_NAME, "h1").text)

    # @parameterized.expand([
    #     ('invalid password', "admin", '123abc', "Invalid credentials"),
    #     ('empty username', '', 'password', "Username cannot be empty"),
    #     ('empty password', 'admin', '', "Password cannot be empty")
    # ])
    @parameterized.expand(read_csv)
    def test_invalid_credentials(self, test_name, username, password, expected_error_message):
        authenticate(self.browser, username=username, password=password)
        message = self.browser.find_elements(By.ID, 'spanMessage')
        self.assertTrue(message)
        self.assertEqual(expected_error_message, message[0].text)

    # def test_empty_username(self):
    #     expected_error_message = "Username cannot be empty"
    #     username = ''
    #     password = 'password'
    #
    #     authenticate(self.browser, username=username, password=password)
    #     message = self.browser.find_elements(By.ID, 'spanMessage')
    #     self.assertTrue(message)
    #     self.assertEqual(expected_error_message, message[0].text)

    # def test_empty_password(self):
    #     expected_error_message = "Password cannot be empty"
    #     username = 'admin'
    #     password = ''
    #
    #     authenticate(self.browser, username=username, password=password)
    #     message = self.browser.find_elements(By.ID, 'spanMessage')
    #     self.assertTrue(message)
    #     self.assertEqual(expected_error_message, message[0].text)


if __name__ == '__main__':
    unittest.main()

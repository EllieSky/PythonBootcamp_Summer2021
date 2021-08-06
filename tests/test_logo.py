import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class LogoTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

    def tearDown(self) -> None:
        self.browser.quit()

    def test_logo_position(self):
        browser = self.browser
        images_found = browser.find_elements(By.TAG_NAME, 'img')
        self.assertTrue(images_found, "Test aborted, no img tag for the logo was located on the page")

        logo = images_found[0]

        size_of_logo = logo.size
        location_of_logo = logo.location   # top left pixel (x,y)
        logo_file_name = logo.get_attribute('src')
        size_of_page = browser.find_element(By.TAG_NAME, 'body').size

        top_left_quadrant_width = size_of_page.get('width') / 2
        top_left_quadrant_height = size_of_page.get('height') / 2

        location_of_logo_bottom_left_x = location_of_logo.get('x') + size_of_logo.get('width')
        location_of_logo_bottom_left_y = location_of_logo.get('y') + size_of_logo.get('height')

        self.assertLess(location_of_logo_bottom_left_y, top_left_quadrant_height)
        self.assertLess(location_of_logo_bottom_left_x, top_left_quadrant_width)

        self.assertIn('logo.png', logo_file_name)

    def test_logo_size(self):
        browser = self.browser
        images_found = browser.find_elements(By.TAG_NAME, 'img')
        self.assertTrue(images_found, "Test aborted, no img tag for the logo was located on the page")

        logo = images_found[0]

        self.assertEqual('283', logo.get_attribute('width'))
        self.assertEqual('56', logo.get_attribute('height'))





if __name__ == '__main__':
    unittest.main()

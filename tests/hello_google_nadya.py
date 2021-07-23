import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


class GoogleSearchTests(unittest.TestCase):
    def test_search_hello(self):
        ChromeDriverManager().install()

        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get("http://www.google.com")
        browser.find_element_by_name("q").send_keys("hello", Keys.ENTER)
        sleep(2)
        actual = browser.find_element_by_name('q').get_attribute('value')
        self.assertEqual('hello', expected)


if __name__ == '__main__':
    unittest.main()

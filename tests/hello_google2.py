import unittest
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def test_search_hello(self):
        # for Firefox use:
        # GeckoDriverManager().install()
        # browser = webdriver.Chrome()

        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get("http://www.google.com")
        browser.find_element_by_name('q').send_keys('hello', Keys.ENTER)
        sleep(2)
        actual = browser.find_element_by_name('q').get_attribute('value')
        self.assertEqual('hello', actual)
        pass


if __name__ == '__main__':
    unittest.main()

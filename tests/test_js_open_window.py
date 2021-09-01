import unittest
from telnetlib import EC

from selenium.webdriver.common.by import By

from fixtures import BaseFixture

class JSOpenWindowTests(BaseFixture):
    def test_js_open_new_window(self):
        self.browser.execute_script("window.alert(arguments[0] + " " + arguments[1]", 'WHat\'s happening?', 'Bob')
        #JS only method
        self.browser.execute_script("document.querySelector('#footer a').click()")
        #or using if need to wait

        footer_link = self.wait.until(EC.ppresense_of_element_located((By.CSS_SELECTOR, '#footer a'))
        # footer_link = self.browser.find_element(By.CSS_SELECTOR, '#footer a')
        #all elements will be passsed - footer_link, "hello", 15
        self.browser.execute_script("arguments[0]", footer_link, "hello", 15)



if __name__ == '__main__':
    unittest.main()

import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures import BaseFixture


class JSOpenWindowTests(BaseFixture):
    def test_js_open_new_window(self):
        self.browser.execute_script("window.alert(arguments[0])", "What's happening?")
        self.wait.until(EC.alert_is_present()).dismiss()

        # JS only method
        # self.browser.execute_script("document.querySelector('#footer a').click()")

        footer_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#footer a')))
        self.browser.execute_script("arguments[0].click()", footer_link)

        current_page_title = self.browser.title
        self.assertEqual('OrangeHRM', current_page_title)

        self.assertEqual(2, len(self.browser.window_handles))

        self.browser.switch_to.window(self.browser.window_handles[-1])

        current_page_title = self.browser.title
        self.assertEqual('OrangeHRM HR Software | Free HR Software | HRMS | HRIS',
                         current_page_title)

        demo_btn = self.browser.find_element(By.CLASS_NAME, 'demo-btn')
        demo_btn.location_once_scrolled_into_view
        button_href = demo_btn.find_element(By.XPATH, ".//..").get_attribute('href')

        # self.browser.switch_to.new_window()
        # self.browser.get(button_href)
        self.browser.execute_script("window.open(arguments[0])", button_href)

        all_windows = self.browser.window_handles
        self.assertEqual(3, len(all_windows))

        self.browser.switch_to.window(all_windows[-1])
        new_page_title = self.browser.title
        self.assertEqual('Sign Up for a Free HR Software Demo | OrangeHRM', new_page_title)

        self.browser.close()

        all_windows = self.browser.window_handles
        self.assertEqual(2, len(all_windows))

        self.browser.switch_to.window(all_windows[1])
        self.browser.close()

        self.browser.switch_to.window(all_windows[0])

        current_page_title = self.browser.title
        self.assertEqual('OrangeHRM', current_page_title)











if __name__ == '__main__':
    unittest.main()

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait

from tests import CHROME_PATH, DOMAIN, ADMIN_USER, DEFAULT_PASSWORD


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_search_by_valid_id(self):
        self.browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        self.browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        self.browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        self.browser.find_element(By.ID, "empsearch_id").send_keys('0001')

        #self.browser.find_element(By.ID, "search_form").submit()
        #or
        self.browser.find_element(By.ID, "searchBtn").click()

        rows = self.browser.find_element(By.XPATH,"//tbody/tr")
        self.assertEqual(1, len(rows))

        self.assertEqual('0001', self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr[1]/td[2]/a').text)
        self.assertEqual('Bob', self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr[1]/td[3]/a').text)
        self.assertEqual('Boss', self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr[1]/td[4]/a').text)
        self.assertEqual('QA Manager', self.browser.find_element(By.XPATH, '//*[@id="resultTable"]/tbody/tr[1]/td[5]').text)


    def test_search_by_valid_id(self):
        browser = self.browser
        browser.find_element(By.ID, "txtUsername").send_keys(ADMIN_USER)
        browser.find_element(By.ID, "txtPassword").send_keys(DEFAULT_PASSWORD)
        browser.find_element(By.ID, "btnLogin").click()

        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))

        browser.find_element(By.ID, 'empsearch_job_title').send_keys("QA Manager")
        #browser.find_element(By.ID, 'empsearch_job_title').click()
        #browser.find_element(By.XPATH,'//*[@id="empsearch_job_title"]/option[8]').click()

        Select(browser.find_element(By.ID, 'empsearch_job_title')).select_by_visible_text("QA Manager")

        self.browser.find_element(By.ID, "search_form").submit()
        # or
        self.browser.find_element(By.ID, "searchBtn").click()

        #rows = self.browser.find_element(By.XPATH, "//tbody/tr")
        job_title_cells = self.browser.find_element(By.XPATH, "//tbody/tr/td[5]")
        for cell in job_title_cells:
            self.assertEqual('QA Manager', cell.text)

        rows = self.browser.find_element(By.XPATH, "//tbody/tr")
        for single_row in rows:
            self.assertEqual('QA Manager', single_row.find_element(By.XPATH, ".//td[5]").text)


    pass





if __name__ == '__main__':
    unittest.main()

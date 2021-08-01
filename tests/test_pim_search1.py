import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from homework_inessa import ID_VALUE
from steps.common import authenticate
from tests import CHROME_PATH, DOMAIN


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=CHROME_PATH)
        self.browser.get(DOMAIN)
        authenticate(self.browser)
        wait = WebDriverWait(self.browser, 7)
        wait.until(expected_conditions.url_contains("/pim/viewEmployeeList"))
    #cleanup after test
    def tearDown(self) -> None:
        self.browser.quit()

    def test_search_by_valid_id(self):
        self.browser.find_element(By.ID, "empsearch_id").send_keys(ID_VALUE)
        self.brower.find_element(By.ID, "searchBtn").click()
#         only a row
        self.browser.find_element(By.XPATH, "//*[@id='resultTable']/tbody/tr")

        rows = self.browser.find_elements(By.XPATH, "//tbody/tr")
        len(rows)
        self.assertEqual(1, len(rows))
        self.assertEqual('0001',self.browser.find_element(By.XPATH, "//*[@id='resultTable]/tbody/tr/td[2]/a").text)
        self.assertEqual('Bob',self.browser.find_element(By.XPATH, "//*[@id='resultTable]/tbody/tr/td[3]/a").text)
        self.assertEqual('Boss',self.browser.find_element(By.XPATH, "//*[@id='resultTable]/tbody/tr/td[4]/a").text)
        self.assertEqual('QA Manager',self.browser.find_element(By.XPATH, "//*[@id='resultTable]/tbody/tr/td[5]").text)

    def test_search_by_job_title(self):
        authenticate(self.browser)



        self.browser.find_element(By.ID, "empsearch_id").send_keys(ID_VALUE)
        # self.browser.find_element(By.ID, "search_form").submit
        self.browser.find_element(By.ID, "searchBtn").click()
#         not preferred methods
        #self.browser.find_element(By.ID, "empsearch_job_title").send_keys("QA Manager")
        # self.browser.find_element(By.XPATH, "//*[@id="empsearch_job_title"]/option[8]").send_keys("QA Manager")
        #preferred method
        Select(self.browser.find_element(By.ID, "empsearch_job_title")).select_by_visible_text("QA Manager")
        self.browser.find_element(By.ID, "searchBtn").click()
         # first way
        # 7:57 PM
         #second way


          #     find elements from 2 criteris job title and employment status
         job_title_cells = self.assertEqual('QA Manager', job_title_cells.find_element(By.XPATH, ".//td[5]"))
         self.assertGreater(len)
         self.assertEqual('QA Manager', job_title_cells.find_element(By.XPATH, ".//td[6]"))


        pass




if __name__ == '__main__':
    unittest.main()

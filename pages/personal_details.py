from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods


class PersonalDetailsPage(BaseMethods):
    pers_det_page = (By.CSS_SELECTOR, ".personalDetails h1")
    job = (By.XPATH, '//*[@id="sidenav"]//a[text()="Job"]')

    def verify_personal_details_page(self):
        return self.get_text(self.pers_det_page)

    def click_job(self):
        self.click_elem(self.job)


from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods


class ActionsChains:
    pass


class TopNavMenu(BaseMethods):
    pim = (By.ID, 'menu_pim_viewPimModule')
    admin = (By.ID, 'menu_admin_viewAdminModule')
    my_info =  (By.ID, 'menu_pim_viewMyDetails')
    user_managment = (By.ID, 'menu_admin_UserManagement')
    configuration_admin = (By.ID, 'menu_admin_Configuration')
    localization =""

    def open_PIM(self):
        self.click_elem()
        pass

    def open_Admin(self):
        self.click_elem()

    def open_My_Info(self):
            self.click_elem()

    def open_Admin_Configuration_Localization(self):
        action = ActionsChains(self.browser)
        action.move_to_element(self.find_elem(self.admin))
        action.move_to_element(self.find_elem(self.user_managment))
        action.move_to_element(self.find_elem(self.configuration_admin))
        action.click(self.find_elem(self.localization))
        action.perform()



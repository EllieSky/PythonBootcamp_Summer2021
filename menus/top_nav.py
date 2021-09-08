from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from test_steps.base_methods import BaseMethods


class TopNavMenu(BaseMethods):
    pim = (By.ID, 'menu_pim_viewPimModule')
    admin = (By.ID, 'menu_admin_viewAdminModule')
    user_management = (By.ID, 'menu_admin_UserManagement')
    configuration_admin = (By.ID, 'menu_admin_Configuration')
    localization = (By.ID, 'menu_admin_localization')
    my_info = (By.ID, 'menu_pim_viewMyDetails')
    time = (By.ID, 'menu_time_viewTimeModule')
    attendance = (By.ID, 'menu_attendance_Attendance')
    punch_in_out = (By.ID, 'menu_attendance_punchIn')
    configuration_pim = (By.ID, 'menu_pim_Configuration')
    termination_reason = (By.ID, 'menu_pim_viewTerminationReasons')

    def open_PIM(self):
        self.click_elem(self.pim)

    def open_Admin(self):
        self.click_elem(self.admin)

    def open_My_Info(self):
        self.click_elem(self.my_info)

    # continue adding other "top menu" items here...

    def open_Admin_Configuration_Localization(self):
        action = ActionChains(self.browser)
        action.move_to_element(self.find_elem(self.admin))
        action.move_to_element(self.find_elem(self.user_management))
        action.move_to_element(self.find_elem(self.configuration_admin))
        action.click(self.find_elem(self.localization))
        action.perform()

    def open_Time_Attendance_PunchInOut(self):
        action = ActionChains(self.browser, duration=1000)
        action.move_to_element(self.find_elem(self.time))
        action.move_to_element(self.find_elem(self.attendance))
        action.move_to_element(self.find_elem(self.punch_in_out))
        action.click().perform()

    def open_PIM_Configuration_TerminationReasons(self):
        ActionChains(self.browser).move_to_element(self.find_elem(self.pim))\
            .move_to_element(self.find_elem(self.configuration_pim)).\
            click(self.find_elem(self.termination_reason)).perform()


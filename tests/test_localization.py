import unittest

from fixtures import AdminUserAuthentication
from menus.top_nav import TopNavMenu
from pages.localization import LocalizationPage
from pages.punch_inout import PunchInOutPage


class LocalizationTests(AdminUserAuthentication):
    def test_localization(self):
        top_nav = TopNavMenu(self.browser)
        local_page = LocalizationPage(self.browser)

        top_nav.open_Admin_Configuration_Localization()
        self.assertEqual(local_page.HEADER, local_page.get_page_header())
        self.assertIn(local_page.PAGE_URL, self.browser.current_url)

    def test_punch_inout(self):
        top_nav = TopNavMenu(self.browser)
        punch_inout = PunchInOutPage(self.browser)

        top_nav.open_Time_Attendance_PunchInOut()
        self.assertEqual(punch_inout.HEADER, punch_inout.get_page_header())
        self.assertIn(punch_inout.PAGE_URL, self.browser.current_url)


if __name__ == '__main__':
    unittest.main()

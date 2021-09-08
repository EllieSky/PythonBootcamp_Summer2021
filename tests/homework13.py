import unittest

from menus.top_nav import TopNavMenu
from pages.termination_reasons import TerminationReasons

"""
Homework:
(Use POM to create the test.)
Login
Got to PIM > Configuration > Termination reasons
Click Add
Enter a new reason : Missing / No-Show
Save
Assert it was created
Select the checkbox next to it
Delete the reason
Assert in was removed
"""

from fixtures import AdminUserAuthentication


class HomeWork13(AdminUserAuthentication):
    def test_home_work(self):
        top_nav = TopNavMenu(self.browser)
        termination_reasons_page = TerminationReasons(self.browser)

        text = 'Missing / No-Show'
        top_nav.open_PIM_Configuration_TerminationReasons()
        self.assertEqual(termination_reasons_page.HEADER, termination_reasons_page.get_page_header())
        termination_reasons_page.add_new_reason(text)
        self.assertTrue(termination_reasons_page.find_required_reason(text))
        termination_reasons_page.remove_reason(text)
        self.assertFalse(termination_reasons_page.find_required_reason(text))


if __name__ == '__main__':
    unittest.main()

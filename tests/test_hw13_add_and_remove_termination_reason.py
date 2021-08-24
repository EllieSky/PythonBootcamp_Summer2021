import unittest

from fixtures import AdminUserAuthentication
from menus.top_nav import TopNavMenu
from pages.add_termination_reason import AddTerminationReasonPage
from pages.termination_reasons import TerminationReasonsPage


class TerminationReasonTests(AdminUserAuthentication):

    def test_termination_reason(self):
        top_nav = TopNavMenu(self.browser)
        termination_page = TerminationReasonsPage(self.browser)
        add_termination_reason = AddTerminationReasonPage(self.browser)

        top_nav.open_PIM_Configuration_Termination_reasons()
        self.assertEqual(termination_page.HEADER, termination_page.get_page_header())
        self.assertIn(termination_page.PAGE_URL, self.browser.current_url)
        termination_page.click_add_btn()

        self.assertEqual(add_termination_reason.HEADER, add_termination_reason.get_page_header())
        self.assertIn(add_termination_reason.PAGE_URL, self.browser.current_url)
        termination_reason = 'Missing / No - Show'
        add_termination_reason.add_reason(termination_reason)

        table_of_reasons = termination_page.get_table_of_reasons().text
        # print(table_of_reasons)
        self.assertIn(termination_reason, table_of_reasons)

        termination_page.remove_reason()
        new_table_of_reasons = termination_page.get_table_of_reasons().text
        # print(new_table_of_reasons)
        self.assertNotIn(termination_reason, new_table_of_reasons)


if __name__ == '__main__':
    unittest.main()

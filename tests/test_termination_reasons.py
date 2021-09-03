import time

from fixtures import AdminUserAuthentication
from menus.top_nav import TopNavMenu
from pages.termination_reasons import TerminationReasonsPage


class TestTerminationReasons(AdminUserAuthentication):
    def setUp(self):
        super().setUp()
        self.top_nav = TopNavMenu(self.browser)
        self.termination_reasons_page = TerminationReasonsPage(self.browser)

    def test_create_and_destroy_termination_reason(self):
        # test_reason_name = 'Missing / No-Show'

        # Random text to prevent colliding with other students
        random_text = str(int(time.time() * 1000))[4:]
        test_reason_name = f'Missing / No-Show ({random_text})'

        # Got to PIM > Configuration > Termination reasons
        self.top_nav.open_pim_configuration_termination_reasons()
        self.assertEqual(self.termination_reasons_page.HEADER, self.termination_reasons_page.get_page_header())

        # Click Add
        # Enter a new reason : Missing / No-Show
        # Save
        self.termination_reasons_page.add_new_reason(test_reason_name)

        # Assert it was created
        self.assertTrue(self.termination_reasons_page.search_reason(test_reason_name))

        # Select the checkbox next to it
        # Delete the reason
        self.termination_reasons_page.delete_reason(test_reason_name)

        # Assert in was removed
        self.assertFalse(self.termination_reasons_page.search_reason(test_reason_name))

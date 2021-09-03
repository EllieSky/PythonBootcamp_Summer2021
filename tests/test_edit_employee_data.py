import os
import unittest
from random import randint

from api.api_requests import Api
from fixtures import AdminUserAuthentication
from tests import PROJ_HOME


class PersonalDetailPage:
    pass


class EditEmployeeDataTests(AdminUserAuthentication):
    def test_edit_employee_middle_name(self):
        file_path = os.path.join(PROJ_HOME, 'data', 'puppy-development.jpg')
        emp_id = f'EMP{randint(10000001,999999999999)}'
        api = Api()
        api.authenticate()
        result = api.add_employee(firstName='Bob', lastName="smith", emp_id=emp_id, profile_img=file_path)
        self.browser.get(result.url)
        emp_details_page = PersonalDetailPage(self.browser)
        emp_details_page.edit()
        emp_details_page.update_personal_details(middle_name='Doe')




if __name__ == '__main__':
    unittest.main()

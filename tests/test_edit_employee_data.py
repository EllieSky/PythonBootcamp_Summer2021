import os
import unittest
from faker import Faker
from dataclasses import dataclass
from random import randint

from bs4 import BeautifulSoup

from api.api_requests import Api
from fixtures import AdminUserAuthentication
from pages.personal_details import PersonalDetailsPage
from tests import PROJ_HOME


@dataclass
class Employee:
    emp_id: str
    first_name: str
    last_name: str


class EditEmployeeDataTests(AdminUserAuthentication):
    f = Faker()

    def setUp(self):
        super(EditEmployeeDataTests, self).setUp()
        file_path = os.path.join(PROJ_HOME, 'data', 'puppy.jpg')

        emp_id = f'EMP{randint(1000001, 9999999)}'
        self.emp = Employee(emp_id, self.f.first_name(), self.f.last_name())

        api = Api()
        api.authenticate()
        result = api.add_employee(firstName=self.emp.first_name, lastName=self.emp.last_name,
                                  emp_id=emp_id, profile_img=file_path)
        self.emp_num = result.url.split('/')[-1]
        self.browser.get(result.url)
        self.api = api

    def tearDown(self) -> None:
        self.api.delete_employee(self.emp_num)
        super(EditEmployeeDataTests, self).tearDown()

    def test_edit_employee_middle_nick_name(self):
        middle_name = self.f.first_name()
        nick_name = self.f.word().title()

        emp_details_page = PersonalDetailsPage(self.browser)
        emp_details_page.edit()
        emp_details_page.update_personal_details(middle_name=middle_name, nick_name=nick_name)
        self.assertIn(self.emp.last_name, emp_details_page.get_profile_pic_header())
        self.assertEqual(f'{self.emp.first_name} {middle_name} {self.emp.last_name}', emp_details_page.get_profile_pic_header())

        # emp_num = emp_details_page.get_employee_number()
        # OR

        response = self.api.get_employee_details(self.emp_num)
        doc = BeautifulSoup(response.text, 'html5lib')
        middle_name_value = doc.find(id=emp_details_page.middle_name_fld[1]).attrs.get('value')
        self.assertEqual(middle_name, middle_name_value)

        nick_name_value = doc.find(id=emp_details_page.nick_name_fld[1]).attrs.get('value')
        self.assertEqual(nick_name, nick_name_value)

    def edit_employee_ssn(self):
        pass

    def edit_employee_profile_photo(self):
        pass





if __name__ == '__main__':
    unittest.main()

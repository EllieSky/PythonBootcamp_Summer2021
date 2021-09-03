import os
from bs4 import BeautifulSoup
from lxml import etree
import requests
from requests_toolbelt import MultipartEncoder

from tests import BASE_URL, PROJ_HOME


class Api:
    # BASE_URL = 'http://hrm-online.portnov.com/symfony/web/index.php'

    post_headers = {
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }

    def get_login_page(self):
        result = self.session.get(url=BASE_URL)
        self.csrf_token = self._get_token_bs4(result.text)
        return result

    def authenticate(self, username='admin', password='password', csrf_token=None):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        if not csrf_token and not hasattr(self, 'csrf_token'):
            self.get_login_page()

        data = {
        # actionID:
            '_csrf_token': csrf_token or self.csrf_token,
            'txtUsername': username,
            'txtPassword': password,
            'Submit': 'LOGIN'
        }

        return self.session.post(url=f'{BASE_URL}/auth/validateCredentials', headers=headers, data=data)

    def add_employee(self, firstName=None, middleName=None,lastName=None, emp_id=None, profile_img=None):
        response = self.session.get(url=BASE_URL + '/pim/addEmployee')
        # self.csrf_token = self._get_token(response.text)
        self.csrf_token = self._get_token_etree(response.text)

        photofile = ('profile', open(profile_img, 'rb'), 'image/jpeg')

        data = {
            'firstName': firstName,
            'middleName': middleName,
            'lastName': lastName,
            'employeeId': str(emp_id),
            'photofile': photofile,
            'user_name': '',
            'user_password': '',
            're_password': '',
            'status': 'Enabled',  # if disable is selected, employee will be deleted
            'empNumber': '',
            '_csrf_token': self.csrf_token,
        }

        mpf = MultipartEncoder(fields=data)

        headers = {
            'Content-Type': mpf.content_type
        }
        return self.session.post(url=BASE_URL + '/pim/addEmployee', headers=headers, data=mpf.to_string())

    def get_employee_details(self, empNumber):
        return self.session.get(url=BASE_URL + f'/pim/viewEmployee/empNumber/{empNumber}')

    def delete_employee(self, empNumber):
        response = self.session.get(url=f'{BASE_URL}/pim/viewEmployeeList')
        default_list_token = self._get_token_etree(response.text, 'defaultList__csrf_token')

        data = {
            'defaultList[_csrf_token]': default_list_token,
            'chkSelectRow[]': str(empNumber)
        }

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        self.session.post(url=BASE_URL + '/pim/deleteEmployees', data=data, headers=headers)

    def _get_token_bs4(self, source, token_id='csrf_token'):
        doc = BeautifulSoup(source, 'html5lib')
        return doc.find(id=token_id).attrs.get('value')

    def _get_token_etree(self, source, token_id='csrf_token'):
        doc = etree.HTML(source)
        return doc.xpath(f"//input[@id='{token_id}']")[0].attrib.get('value')




def write_to_file(source):
    file = open(os.path.join(PROJ_HOME, 'test_output', 'request_response.html'), 'w')
    file.write(source)
    file.close()



import requests
import json as JSON


class RecruitAPI:
    post_headers = {
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.session = requests.Session()

    def login(self, email="student@example.com", password="welcome"):

        json = {
            "email": email,
            "password": password
        }

        result = self.session.post(
            url='https://recruit-portnov.herokuapp.com/recruit/api/v1/login',
            headers=self.post_headers,
            json=json
        )

        token: str = JSON.loads(result.text).get('token')
        self.session.headers = {"authorization": f"Bearer {token}"}

    def post_positions(self, title='', **kwargs):
        default = 'string'
        json = {
            "title": title,
            "address": kwargs.get('address'),
            "city": kwargs.get('city'),
            "state": kwargs.get('state'),
            "zip": kwargs.get('zip'),
            "description": kwargs.get('description'),
            "dateOpen": kwargs.get('dateOpen'),
            "company": kwargs.get('company')
        }

        return self.session.post(
            url='https://recruit-portnov.herokuapp.com/recruit/api/v1/positions',
            headers=self.post_headers,
            json=json)



# For debugging only!!!
api = RecruitAPI()
api.login()
result = api.post_positions(title='API Automation Guru', state='CA')
# For homework please create a unittest and import this class to use it.
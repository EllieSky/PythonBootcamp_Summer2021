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

    def post_position(self, title='', **kwargs):
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

    def put_position(self, id, **kwargs):
        json = {
            "title": kwargs.get('title'),
            "address": kwargs.get('address'),
            "city": kwargs.get('city'),
            "state": kwargs.get('state'),
            "zip": kwargs.get('zip'),
            "description": kwargs.get('description'),
            "dateOpen": kwargs.get('dateOpen'),
            "company": kwargs.get('company')
        }

        return self.session.put(
            url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}',
            headers=self.post_headers,
            json=json)

    def get_position(self, id):
        return self.session.get(
            url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}',
            headers=self.post_headers)

    def delete_position(self, id):
        return self.session.delete(
            url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}',
            headers=self.post_headers)
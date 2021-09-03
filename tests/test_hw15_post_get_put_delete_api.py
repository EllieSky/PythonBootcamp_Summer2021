import json as JSON
import unittest

import requests


class RecruitAPITest:
    post_headers = {
        "Content-Type": "application/json"
    }

    def __init__(self):
        self.session = requests.Session()

    def login(self, email='student@example.com', password='welcome'):
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
        json = {
            "title": title,
            "address": kwargs.get('address'),
            "city": kwargs.get('city'),  # or kwargs['city']
            "state": kwargs.get('state'),
            "zip": kwargs.get('zip'),
            "description": kwargs.get('description'),
            "dateOpen": kwargs.get('dateOpen'),
            "company": kwargs.get('company')
        }

        result = self.session.post(
            url='https://recruit-portnov.herokuapp.com/recruit/api/v1/positions',
            headers=self.post_headers,
            json=json
        )

        position_ID = JSON.loads(result.text).get('id')
        return position_ID

    def get_position(self, id):
        return self.session.get(
            url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}',
            headers=self.post_headers
        )

    def put_position(self, id, title, **kwargs):
        json = {
            "title": title,
            "address": kwargs.get('address'),
            "city": kwargs.get('city'),  # or kwargs['city']
            "state": kwargs.get('state'),
            "zip": kwargs.get('zip'),
            "description": kwargs.get('description'),
            "dateOpen": kwargs.get('dateOpen'),
            "company": kwargs.get('company')
        }
        return self.session.put(
            url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}',
            headers=self.post_headers,
            json=json
        )

    def delete_position(self, id):
        return self.session.delete(
            url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}',
            headers=self.post_headers
        )


class TestCreateUpdateDeletePosition(unittest.TestCase):
    def test_create_update_delete_position(self):
        api = RecruitAPITest()

        # authenticate
        api.login()

        # Create a new position and store the positions ID
        position = api.post_positions(title='QA engineer in Test', city='Dallas')

        # Then check the position has been created
        get_position = api.get_position(position)
        self.assertEqual('QA engineer in Test', JSON.loads(api.get_position(position).text).get('title'))
        self.assertEqual('Dallas', JSON.loads(api.get_position(position).text).get('city'))

        # Update the position with additional details
        api.put_position(position, title='QA in Test', city='Richardson', state='TX')

        # Check the position has been updated
        get_position = api.get_position(position)
        self.assertEqual(200, get_position.status_code)
        self.assertEqual('QA in Test', JSON.loads(api.get_position(position).text).get('title'))
        self.assertEqual('Richardson', JSON.loads(api.get_position(position).text).get('city'))
        self.assertEqual('TX', JSON.loads(api.get_position(position).text).get('state'))

        # Delete the position
        api.delete_position(position)

        # Check that it has been deleted
        get_position = api.get_position(position)
        self.assertEqual(400, get_position.status_code)


if __name__ == '__main__':
    unittest.main()

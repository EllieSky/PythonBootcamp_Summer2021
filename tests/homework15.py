import unittest

import requests
import json as JSON

"""
Using the careers-Portnov site above and the swagger documentation 
for the site api, create a scrip which uses requests package and not webdriver to: 
- authenticate
- create a new position and store the positions ID
- then checks the position has been created
- updates the position with additional details
- checks the position has been updated
- deletes the position
- checks that it has been deleted
"""


class RecruitAPI:
    json_headers = {"Content-Type": "application/json"}

    def __init__(self):
        self.session = requests.Session()

    def login(self, email='student@example.com', password='welcome'):
        json = {"email": email, "password": password}
        authentication = self.session.post(
            url='https://recruit-portnov.herokuapp.com/recruit/api/v1/login',
            headers=self.json_headers,
            json=json
        )
        token = JSON.loads(authentication.text).get('token')
        self.session.headers = {"authorization": f"Bearer {token}"}

    def post_new_position(self, title, **kwargs):
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
        post_result = self.session.post(
            url='https://recruit-portnov.herokuapp.com/recruit/api/v1/positions',
            headers=self.json_headers,
            json=json
        )
        position_id = JSON.loads(post_result.text).get('id')
        return position_id

    def get_position(self, id):
        return self.session.get(url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}')

    def edit_position(self, id, **kwargs):
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
            headers=self.json_headers,
            json=json
        )

    def delete_position(self, id):
        return self.session.delete(
            url=f'https://recruit-portnov.herokuapp.com/recruit/api/v1/positions/{id}'
        )


class Homework15(unittest.TestCase):
    def test_creation_updating_deleting_position_cycle(self):
        api = RecruitAPI()

        api.login(email='student@example.com', password='welcome')
        position_id = api.post_new_position(title='IT guru',
                                            address='1 Galaxy Way',
                                            city='Mountain View',
                                            state='CA',
                                            zip='94041',
                                            description='Know everything and work 24/7',
                                            dateOpen='05/10/2021',
                                            company='Galaxy Solutions LLC'
                                            )
        self.assertEqual(200, api.get_position(position_id).status_code)
        api.edit_position(position_id, title='Junior specialist', description='None')
        self.assertEqual('Junior specialist', JSON.loads(api.get_position(position_id).text).get('title'))
        self.assertEqual('None', JSON.loads(api.get_position(position_id).text).get('description'))
        api.delete_position(position_id)
        self.assertEqual(400, api.get_position(position_id).status_code)


if __name__ == '__main__':
    unittest.main()

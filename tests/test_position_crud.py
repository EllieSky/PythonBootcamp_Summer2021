import json
import time
import unittest

from tests.recruit_api import RecruitAPI


class MyRecruitAPI(unittest.TestCase):
    def setUp(self):
        self.api = RecruitAPI()

        # Authenticate
        self.api.login()

    def test_create_update_delete_position(self):
        random_text = str(int(time.time() * 1000))[4:]
        random_position_name = f"Marleg Test Position {random_text}"

        self.payload = {
            "city": "Malibu",
            "state": "CA",
            "zip": "90210",
            "description": "Best job in the world!"
        }

        # Create a new position and store the positions ID
        post_response = self.api.post_positions(random_position_name, **self.payload)
        self.assertEqual(201, post_response.status_code)

        self.position_id: int = json.loads(post_response.text).get('id')

        # Then checks the position has been created
        get_response = self.api.get_positions(self.position_id)
        self.assertEqual(201, post_response.status_code)

        get_position_name: str = json.loads(get_response.text).get('title')
        self.assertEqual(random_position_name, get_position_name)

        self.payload = {
            "city": "New York",
            "state": "NY",
            "zip": "10024",
            "description": "Still the best job in the world!"
        }
        # Updates the position with additional details
        put_response = self.api.put_positions(self.position_id, **self.payload)
        self.assertEqual(200, put_response.status_code)

        # Checks the position has been updated
        get_position_city: str = json.loads(put_response.text).get('city')
        self.assertEqual(self.payload["city"], get_position_city)

        # Deletes the position
        delete_response = self.api.delete_positions(self.position_id)
        self.assertEqual(204, delete_response.status_code)

        # Checks that it has been deleted
        get_response = self.api.get_positions(self.position_id)
        self.assertEqual(400, get_response.status_code)


if __name__ == '__main__':
    unittest.main()

import json
import unittest
import requests
from parameterized import parameterized


class FoothillApiTests(unittest.TestCase):
    def get_foothill_course_search(self):
        return requests.get(url='https://catalog.foothill.edu/course-search/')

    def post_foothill_course_search(self, keyword=None, page=None, route=None, payload=None, **params):
        default_params = {
            'page': page or 'fose',
            # 'page': page if page is not None else None,
            'route': route or 'search',
            'keyword': keyword
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)'
                          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/json'
        }

        json = {
            "other": {"srcdb": ""},
            "criteria": [
                {"field": "keyword", "value": keyword}
            ]
        }

        params = params if params is not None else default_params
        data = payload if payload is not None else json

        return requests.post(url='https://catalog.foothill.edu/course-search/api/',
                             params=params, headers=headers, json=data)


    def test_foothill_catalog_api(self):
        response = self.get_foothill_course_search()
        self.assertEqual(200, response.status_code)
        self.assertIn('/course-search/', response.url)

        self.assertIn('COURSE SEARCH', response.text)

    def test_search_course_catalogue(self):
        result = self.post_foothill_course_search("math")
        search_results = json.loads(result.text).get('results')
        found = False
        for i in search_results:
            if i.get('code') == 'MATH 180':
                found = True
                break
        self.assertTrue(found, "MATH 180 not found")
        classes = list(x.get('code') for x in search_results)
        self.assertIn('MATH 180', classes)
        self.assertIn('MATH 10', classes)


    @parameterized.expand([
        ('no_keyword', None, None, None, '{"fatal":"criterion.value is null"}')
    ])
    def test_search(self, test_name, keyword, route, page, expected_output):
        result = self.post_foothill_course_search(keyword, page, route)
        self.assertEqual(expected_output, result.text)

    def test_search_bad_route(self):
        result = self.post_foothill_course_search(keyword='art', route='BAD')
        self.assertEqual('{"fatal":"Unknown route \\"BAD\\""}', result.text)

    def test_search_empty_page(self):
        result = self.post_foothill_course_search(keyword='art', page=' ')
        self.assertEqual('', result.text)

    def test_search_bad_payload(self):
        payload = {}
        result = self.post_foothill_course_search(keyword='art', payload=payload)
        self.assertEqual('{"fatal":"searchData.other is undefined"}', result.text)

    def test_search_partial_payload(self):
        keyword = 'art'
        payload = {
            "other": '{"dbsrc": ""}',
            "criteria": [
                {"field": "keyword", "value": keyword}
            ]
        }
        result = self.post_foothill_course_search(keyword=keyword, payload=payload)
        self.assertEqual('{"fatal":"searchData.other is undefined"}', result.text)

    def test_search_bad_params(self):
        result = self.post_foothill_course_search(fruit='kiwi', boy='male')
        self.assertEqual('', result.text)

if __name__ == '__main__':
    unittest.main()

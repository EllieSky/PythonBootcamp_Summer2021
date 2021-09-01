import unittest
import requests


def search_course_catalogue(keyword=None, page=None, route=None, payload=None, **params):
    payload = payload if payload is not None else {
        "other": {"srcdb": ""},
        "criteria": [
            {"field": "keyword", "value": str(keyword)}
        ]
    }

    default_params = {
        'page': page if page is not None else 'fose',
        'route': route if route is not None else 'search',
        'keyword': keyword if keyword is not None else ''
    }

    params = params if params else default_params
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/92.0.4515.131 Safari/537.36",
        "Content-Type": "application/json"}

    return requests.post(url='https://catalog.foothill.edu/course-search/api/', headers=header, params=params,
                         json=payload)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        response = requests.get(url='https://catalog.foothill.edu/course-search/api/', )
        self.assertEqual(200, response.status_code)
        self.assertIn('/course-search/', response.url)
        self.assertIn('COURSE SEARCH', response.text)


if __name__ == '__main__':
    unittest.main()

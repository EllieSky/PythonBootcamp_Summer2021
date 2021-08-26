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


class APITests(unittest.TestCase):
    def test_1_response_with_empty_input(self):
        self.assertEqual(200, search_course_catalogue().status_code)

    def test_2_response_with_given_keyword(self):
        self.assertIn("ORGANIC CHEMISTRY", search_course_catalogue(keyword='chem').text)
        self.assertEqual(200, search_course_catalogue(keyword='chem').status_code)

    def test_3_response_with_given_keyword_and_payload(self):
        p = {
            "other": {"srcdb": "hi"},
            "criteria": [
                {"field": "keyword", "value": "hi"}
            ]
        }
        text = "Could not execute database query: Cannot open database"
        self.assertIn(text, search_course_catalogue(keyword='chem', payload=p).text)
        self.assertEqual(200, search_course_catalogue(keyword='chem', payload=p).status_code)

    def test_4_response_with_given_parameters(self):
        param = {'page': 'fose', 'route': 'find', 'keyword': 'math'}
        self.assertEqual('', search_course_catalogue(param=param).text)
        self.assertEqual(200, search_course_catalogue(param=param).status_code)

    def test_5_response_with_given_keyword_and_parameters(self):
        param = {'page': 'fose', 'route': 'find', 'keyword': 'math'}
        self.assertEqual(200, search_course_catalogue(keyword='math', param=param).status_code)

    def test_6_response_with_sql_input(self):
        self.assertIn('"count":0', search_course_catalogue("SELECT * FROM USERS").text)
        self.assertEqual(200, search_course_catalogue("SELECT * FROM USERS").status_code)

    def test_7_response_with_non_required_parameter(self):
        self.assertIn('"count":0', search_course_catalogue({'hi': 'HI'}).text)
        self.assertEqual(200, search_course_catalogue({'hi': 'HI'}).status_code)

    def test_8_response_with_keyword_with_special_symbol(self):
        self.assertIn("ORGANIC CHEMISTRY", search_course_catalogue(keyword='chem@#$').text)
        self.assertEqual(200, search_course_catalogue(keyword='chem@#$').status_code)

    def test_9_response_with_given_route_and_keyword(self):
        self.assertIn('Unknown route', search_course_catalogue(route='find', keyword='chem').text)
        self.assertEqual(200, search_course_catalogue(route='find', keyword='chem').status_code)

    def test_10_response_with_given_page_and_keyword(self):
        self.assertIn('', search_course_catalogue(page='first', keyword='bio').text)
        self.assertEqual(200, search_course_catalogue(page='first', keyword='bio').status_code)


if __name__ == '__main__':
    unittest.main()

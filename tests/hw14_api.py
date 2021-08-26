import requests
import unittest


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


class SearchCourseCatalogueTests(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(200, search_course_catalogue().status_code)

    def test_keyword(self):
        response = search_course_catalogue(keyword='bio')
        self.assertEqual(200, response.status_code)
        self.assertIn('ANTHROPOLOGY', response.text)

    def test_page(self):
        response = search_course_catalogue(page='abc')
        self.assertEqual(200, response.status_code)
        self.assertEqual('', response.text)

    def test_route(self):
        response = search_course_catalogue(route='abc')
        self.assertEqual(200, response.status_code)
        self.assertIn('Unknown route', response.text)

    def test_payload(self):
        response = search_course_catalogue(payload={"other":{"srcdb":""},"criteria":[{"field":"keyword","value":"painting"},{"field":"subject","value":"ART"}]})
        self.assertEqual(200, response.status_code)
        self.assertIn('DIGITAL PAINTING', response.text)




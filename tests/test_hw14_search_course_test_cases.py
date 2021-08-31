import json
import unittest
import requests
from parameterized import parameterized


class FoothillSearchApiTests(unittest.TestCase):

    def get_foothill_course_search(self):
        return requests.get(url='https://catalog.foothill.edu/course-search/')

    def search_course_catalogue(self, keyword=None, page=None, route=None, payload=None, **params):
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
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/92.0.4515.131 Safari/537.36",
            "Content-Type": "application/json"}

        return requests.post(url='https://catalog.foothill.edu/course-search/api/', headers=headers, params=params,
                             json=payload)

    #negative test_cases:
    @parameterized.expand([
        # 0,1 negative page:
        ('empty_page', 'astronomy', 'search', '',   ''),
        ('char_in_page', 'astronomy', 'search', '!@#$%^', ''),
        # 2,3 negative route:
        ('empty_route', 'astronomy', '', 'fose', '{"fatal":"No route specified"}'),
        ('wrong_route', 'astronomy', 'way', 'fose', '{"fatal":"Unknown route \\"way\\""}'),
        # 4,5 negative keyword:
        ('keyword_char', '!@#$%^&*', 'search', 'fose', '{"fatal":"Could not parse incoming payload as JSON"}'),
        ('empty_keyword', None, 'search', 'fose', '{"srcdb":"2021","count":0,"results":[]}'),
        # 6 negative empty page, keyword:
        ('empty_page_keyword', '', 'search', '', ''),
        # 7 negative empty route, keyword:
        ('empty_route_keyword', '', '', 'fose', '{"fatal":"No route specified"}'),
        # 8 negative empty page, route, keyword:
        ('empty_route_page_keyword', '', '', '', ''),
        # 9 negative empty route, keyword:
        ('empty_route_keyword',  '', '', 'fose', '{"fatal":"No route specified"}'),
        # 10 negative wrong page, route, keyword:
        ('wrong_route_page_keyword', 'nothing', 'flood', 'application', ''),
    ])
    def test_post_negative_test_cases(self, test_name, keyword, route, page, expected_output):
        result = self.search_course_catalogue(keyword, page, route)
        self.assertEqual(expected_output, result.text)

        # negative page:
    # def test_post_search_empty_page(self):
    #     result = self.search_course_catalogue(page='', route='search', keyword='astronomy')
    #     self.assertEqual('', result.text)

    # def test_post_search_char_in_page(self):
    #     result = self.search_course_catalogue(page='!@#$%^', keyword='astronomy')
    #     self.assertEqual('', result.text)

         #negative route:
    # def test_post_search_empty_route(self):
    #     result = self.search_course_catalogue(page='fose', route='', keyword='astronomy')
    #     self.assertEqual('{"fatal":"No route specified"}', result.text)
    #
    # def test_post_search_wrong_route(self):
    #     result = self.search_course_catalogue(keyword='astronomy', route='way')
    #     self.assertEqual('{"fatal":"Unknown route \\"way\\""}', result.text)

        # negative keyword:
    # def test_post_search_empty_keyword(self):
    #     result = self.search_course_catalogue(keyword='')
    #     self.assertEqual('{"srcdb":"2021","count":0,"results":[]}', result.text)
    #
    # def test_post_search_keyword_char(self):
    #     result = self.search_course_catalogue(keyword='!@#$%^&*')
    #     self.assertEqual('{"fatal":"Could not parse incoming payload as JSON"}', result.text)

        # negative empty page, keyword:
    # def test_post_search_empty_page_keyword(self):
    #     result = self.search_course_catalogue(keyword='', page='')
    #     self.assertEqual('', result.text)

        # negative empty route, keyword:
    # def test_post_search_empty_route_keyword(self):
    #     result = self.search_course_catalogue(keyword='', route='')
    #     self.assertEqual('{"fatal":"No route specified"}', result.text)

        # negative page, route, keyword:
    # def test_post_search_empty_route_page_keyword(self):
    #     result = self.search_course_catalogue(keyword='', route='', page='')
    #     self.assertEqual('', result.text)
    #
    # def test_post_search_wrong_route_page_keyword(self):
    #     result = self.search_course_catalogue(keyword='nothing', route='flood', page='application')
    #     self.assertEqual('', result.text)


if __name__ == '__main__':
    unittest.main()

import json
import unittest
import requests
from parameterized import parameterized


class FoothillApitests(unittest.TestCase):

    def get_foothil_catalog_search(self):
        return requests.get(url='https://catalog.foothill.edu/course-search/')

    def post_foothill_catalog_search(self,keyword=None, page=None, route=None):

        params = {"page": page or 'fose',
                "route": route or 'search',
        "keyword": keyword
        }
        headers  = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' ,
            'Content-Type': 'application/json'
        }

        json = {
            "other": {"srcdb": ""},
            "criteria": [
                {"field": "keyword", "value": keyword}
            ]
        }


        return requests.post(url='https://catalog.foothill.edu/course-search/api/', params=params, headers=headers, json=json)

        '''
        curl 'https://catalog.foothill.edu/course-search/api/?page=fose&route=search&keyword=math' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://catalog.foothill.edu' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://catalog.foothill.edu/course-search/' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Cookie: __utma=174661941.871701803.1629863410.1629863410.1629863410.1; __utmz=174661941.1629863410.1.1.utmccn=(referral)|utmcsr=google.com|utmcct=/|utmcmd=referral; _fbp=fb.1.1629863410596.1889999916' \
  --data-raw '%7B%22other%22%3A%7B%22srcdb%22%3A%22%22%7D%2C%22criteria%22%3A%5B%7B%22field%22%3A%22keyword%22%2C%22value%22%3A%22math%22%7D%5D%7D' \
  --compressed
        :return: 
        '''




    def test_foothill_catalog_api(self):
        response = self.get_foothil_catalog()
        self.assertEqual(200, response.status_code)
        self.assertIn('/course-search/', response.url)
        self.assertIn('COURSE SEARCH', response.text)

    def test_search_course_catalogue(self):
        result = self.post_foothill_catalog_search()
        search_results = json.loads(result.text).get('results') #extract results from a search result and check if 1 class in there
        found = False
        for i in search_results:
            if i.get('code') == 'MATH 180':
                found = True
        #few classes more efficient, run loop and assert each value
        self.assertTrue(found, "MATH 180 not found")

        classes = list(x.get('code') for x in search_results)
        self.assertIn('MATH 180', classes)
        self.assertIn('MATH 10', classes)

    @parameterized.expand([
        ('no keyword',None,None,None,{"fatal":"criterion.value is null"})

    ])
    def test_search_no_keyword(self):
        result = self.post_foothill_catalog_search()
        self.assertEqual(expected_output, result.text)


    def test_search_no_keyword(self):
        result = self.post_foothill_catalog_search(keyword='art', route='BAD')
        self.assertEqual('{"fatal":"Unknown route \\"BAD\\""}', result.text)

    def test_search_empty_page(self):
        result = self.post_foothill_catalog_search(keyword='art', page='')
        self.assertEqual('', result.text)


if __name__ == '__main__':
    unittest.main()

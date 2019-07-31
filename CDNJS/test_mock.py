import unittest
from unittest.mock import patch, Mock
# from CDNJS.conftest import human_output
import requests

from CDNJS.conftest import human_output, base_url


class BasicTests(unittest.TestCase):
    @patch('conftest.human_output')
    def test_human_output(self, mock_human_output):
        headers = {'Content-Type': 'text/html; charset=utf-8'}
        mock_human_output.return_value = Mock()
        mock_human_output.return_value.json.return_value = headers
        response = human_output()
        self.assertEqual(response.headers['Content-Type'], headers['Content-Type'])
        self.assertEqual(response.status_code, 200)

    @patch('conftest.name')
    def test_name(self, mock_name):
        name = [1140]
        headers = {'Content-Type': 'text/html; charset=utf-8'}
        mock_name.return_value = Mock()
        mock_name.return_value.json.return_value = name
        url = base_url + "/1140"
        response = requests.get(url)
        self.assertEqual(response.headers['Content-Type'], headers['Content-Type'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1140, name)



if __name__ == "__main__":
    unittest.main()

# @pytest.mark.parametrize("name, ", ["/1140"])
# def test_name(base_url, name):
#     """Checking that search by name return is appropriate data"""
#     url = base_url + str(name)
#     resp = requests.get(url)
#     print(url)
#     j = json.loads(resp.content)
#     print(j)
#     assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'
#     assert resp.status_code == 200
#     assert '1140' in j['name']
#
#
# @mark.xfail
# def test_search_query(search_query):
#     """Checking that results is appropriate to search query"""
#     print(search_query.headers['Content-Type'])
#     print(search_query.status_code)
#     print(search_query.url)
#     j = json.loads(search_query.content)
#     name_values = [el['name'] for el in j['results']]
#     print(name_values)
#     assert 'zoom' in name_values
#     assert search_query.headers['Content-Type'] == 'application/json; charset=utf-8'
#     assert search_query.status_code == 200
#
#
# def test_fields(fields):
#     """Checking that jquery returns fields"""
#     print(fields.headers['Content-Type'])
#     print(fields.status_code)
#     print(fields.url)
#     j = json.loads(fields.content)
#     print(type(j))
#     print(j)
#     assert j['name'] == 'jquery'
#     assert j['filename'] == 'jquery.min.js'
#     assert j['version'] == '3.4.1'
#     assert fields.headers['Content-Type'] == 'application/json; charset=utf-8'
#     assert fields.status_code == 200
#
#
# def test_search_query_human_readable(search_query_human_readable):
#     """Checking that query returns in HTML"""
#     print(search_query_human_readable.url)
#     print(search_query_human_readable.headers['Content-Type'])
#     print(search_query_human_readable.status_code)
#     print(type(search_query_human_readable.raw))
#     assert search_query_human_readable.headers['Content-Type'] == 'text/html; charset=utf-8'
#     assert search_query_human_readable.status_code == 200
#
#
# def test_search_query_fields(search_and_fields):
#     """Checking that search with fields returns correctly"""
#     print(search_and_fields.headers['Content-Type'])
#     print(search_and_fields.status_code)
#     print(search_and_fields.url)
#     j = json.loads(search_and_fields.content)
#     print(type(j))
#     len_values = [len(v) for v in j['results']]
#     print(random.choice(len_values))
#     assert random.choice(len_values) == 4
#     for i in j["results"]:
#         print(i['version'])
#         print(i['description'])
#     assert 'description' in i
#     assert 'version' in i
#     assert "description" in i
#     name_values = [el['name'] for el in j['results']]
#     print(name_values)
#     assert 'zoom' in name_values
#
# @mark.xfail
# def test_search_and_assets(search_and_assets):
#     """Checking that search with fields returns correctly"""
#     print(search_and_assets.headers['Content-Type'])
#     print(search_and_assets.status_code)
#     print(search_and_assets.url)
#     j = json.loads(search_and_assets.content)
#     print(type(j))
#     for i in j["results"]:
#         print(len(i['assets']))
#     assert 'assets' in i
#     name_values = [el['name'] for el in j['results']]
#     print(name_values)
#     assert 'zoom' in name_values

"""Test for api.cdnjs"""
import json
import random
import requests
import pytest
from pytest import mark


def test_human_output(human_output):
    """Checking that response is appropriate content-type for human readable query"""
    print(human_output.url)
    print(human_output.headers['Content-Type'])
    print(human_output.status_code)
    print(type(human_output.raw))
    assert human_output.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert human_output.status_code == 200


@pytest.mark.parametrize("name, ", ["/1140"])
def test_name(base_url, name):
    """Checking that search by name return is appropriate data"""
    url = base_url + str(name)
    resp = requests.get(url)
    print(url)
    j = json.loads(resp.content)
    print(j)
    assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert resp.status_code == 200
    assert '1140' in j['name']


@mark.xfail
def test_search_query(search_query):
    """Checking that results is appropriate to search query"""
    print(search_query.headers['Content-Type'])
    print(search_query.status_code)
    print(search_query.url)
    j = json.loads(search_query.content)
    name_values = [el['name'] for el in j['results']]
    print(name_values)
    assert 'zoom' in name_values
    assert search_query.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert search_query.status_code == 200


def test_fields(fields):
    """Checking that jquery returns fields"""
    print(fields.headers['Content-Type'])
    print(fields.status_code)
    print(fields.url)
    j = json.loads(fields.content)
    print(type(j))
    print(j)
    assert j['name'] == 'jquery'
    assert j['filename'] == 'jquery.min.js'
    assert j['version'] == '3.4.0'
    assert fields.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert fields.status_code == 200


def test_search_query_human_readable(search_query_human_readable):
    """Checking that query returns in HTML"""
    print(search_query_human_readable.url)
    print(search_query_human_readable.headers['Content-Type'])
    print(search_query_human_readable.status_code)
    print(type(search_query_human_readable.raw))
    assert search_query_human_readable.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert search_query_human_readable.status_code == 200


@mark.xfail
def test_search_query_fields(search_and_fields):
    """Checking that search with fields returns correctly"""
    print(search_and_fields.headers['Content-Type'])
    print(search_and_fields.status_code)
    print(search_and_fields.url)
    j = json.loads(search_and_fields.content)
    print(type(j))
    len_values = [len(v) for v in j['results']]
    print(random.choice(len_values))
    assert random.choice(len_values) == 4
    for i in j["results"]:
        print(i['version'])
        print(i['description'])
    assert 'description' in i
    assert 'version' in i
    assert "description" in i
    name_values = [el['name'] for el in j['results']]
    print(name_values)
    assert 'zoom' in name_values

@mark.xfail
def test_search_and_assets(search_and_assets):
    """Checking that search with fields returns correctly"""
    print(search_and_assets.headers['Content-Type'])
    print(search_and_assets.status_code)
    print(search_and_assets.url)
    j = json.loads(search_and_assets.content)
    print(type(j))
    for i in j["results"]:
        print(len(i['assets']))
    assert 'assets' in i
    name_values = [el['name'] for el in j['results']]
    print(name_values)
    assert 'zoom' in name_values

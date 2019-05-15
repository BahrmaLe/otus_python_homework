"""Test for api.openbrewerydb"""
import json
import requests
import pytest
from pytest import mark


@pytest.mark.parametrize("state, ", ["/breweries?by_state=new_york"])
def test_state_search(base_url, state):
    """Checking that search by state is correctly"""
    url = base_url + str(state)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    for i in j:
        assert i['state'] == 'New York'
    print(i['state'])
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'state']))
    print(s)
    assert s == c


@pytest.mark.parametrize("name, ", ["/breweries?by_name=cooper"])
def test_name_search(base_url, name):
    """Checking that search by name is correctly"""
    url = base_url + str(name)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    for i in j:
        print(i['name'])
        assert 'Cooper' in i['name']
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'name']))
    print(s)
    assert s == c


@pytest.mark.parametrize("tag, ", ["/breweries?by_tag=patio"])
def test_tag_search(base_url, tag):
    """Checking that search by tag is correctly"""
    url = base_url + str(tag)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    for i in j:
        print(i['tag_list'])
        assert 'patio' in i['tag_list']
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'tag_list']))
    print(s)
    assert s == c


@pytest.mark.parametrize("name_state, ", ["/breweries?by_name=cooper&by_state=new_york"])
def test_name_state_search(base_url, name_state):
    """Checking that search by name and state is correctly"""
    url = base_url + str(name_state)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    for i in j:
        print(i['name'])
        print(i['state'])
        assert 'Cooper' in i['name']
        assert 'New York' in i['state']
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'state']))
    n = (len([k for d in j for k in d.keys() if k == 'name']))
    print(s)
    print(n)
    assert s == c
    assert n == c


@pytest.mark.parametrize("state_sort_by_type_name, ", ["/breweries?by_state=ohio&sort=type,-name"])
def test_state_search_sort_name(base_url, state_sort_by_type_name):
    """Checking that search by state and sorting by type and name descending is correctly"""
    url = base_url + str(state_sort_by_type_name)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    for i in j:
        print(i['name'])
        print(i['state'])
        print(i['brewery_type'])
        assert 'Ohio' in i['state']
        assert 'brewpub' in i['brewery_type']
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'state']))
    print(s)
    assert s == c
    d = j
    asclist = sorted(j, key=lambda k: k['name'])
    desclist = sorted(j, key=lambda k: k['name'], reverse=True)
    assert d == desclist
    assert d != asclist


@pytest.mark.parametrize("pagination, ", ["/breweries?page=2&per_page=30"])
def test_pagination(base_url, pagination):
    """Checking that pagination is correctly"""
    url = base_url + str(pagination)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'id']))
    print(s)
    assert s == c
    assert c == 30


@pytest.mark.parametrize("pagination, ", ["/breweries?page=2"])
def test_pagination_by_default(base_url, pagination):
    """Checking that pagination by default is correctly"""
    url = base_url + str(pagination)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'id']))
    print(s)
    assert s == c
    assert c == 20


@pytest.mark.parametrize("pagination, ", ["/breweries?page=2&per_page=60"])
def test_max_pagination(base_url, pagination):
    """Checking that max pagination is 50 correctly"""
    url = base_url + str(pagination)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    c = len(j)
    print(c)
    assert resp.status_code == 200, resp.text
    s = (len([k for d in j for k in d.keys() if k == 'id']))
    print(s)
    assert s == c
    assert c == 50


@pytest.mark.parametrize("pagination, ", ["/breweries/5494"])
def test_id_search(base_url, pagination):
    """Checking that search by id is correctly"""
    url = base_url + str(pagination)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    print(j)
    c = len(j)
    print(c)
    assert j['id'] == 5494
    assert type(j) is dict
    assert resp.status_code == 200, resp.text


@pytest.mark.parametrize("autocomplete, ", ["/breweries/autocomplete?query=dog"])
def test_autocomplete_listing(base_url, autocomplete):
    """Checking that autocomplete return dict max two elements and correspond to query"""
    url = base_url + str(autocomplete)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    print(j)
    c = len(j)
    print(c)
    for i in j:
        assert 'Dog' in i['name']
        a = len(i)
        assert a == 2
        print(len(i))
        print(i)
    assert resp.status_code == 200, resp.text


@mark.xfail
@pytest.mark.parametrize("query, ", ["/breweries/search?query=dog"])
def test_search_query(base_url, query):
    """Checking that search query returns correspond list"""
    url = base_url + str(query)
    resp = requests.get(url)
    j = json.loads(resp.text)
    print(type(j))
    print(j)
    c = len(j)
    print(c)
    for i in j:
        assert 'Dog' in i['name']
    assert resp.status_code == 200, resp.text

"""Fixtures for tests.py """
import pytest
import requests

BASE_URL = "https://api.cdnjs.com/libraries"
querystring = {"output": "human"}
query = {"search": "[zoom]"}
fieldstring = {"fields": 'name,filename,version'}
url = {"search": "[zoom]", "output": "human"}
search_query_fields = {"search": "[zoom]", "fields": "version,description"}
search_assets = {"search": "[zoom]", "fields": "assets"}


@pytest.fixture(params=search_assets)
def search_and_assets():
    """Get request with search assets params"""
    response = requests.request("GET", BASE_URL, params=search_assets)
    return response


@pytest.fixture(params=search_query_fields)
def search_and_fields():
    """Get request with search fields params"""
    response = requests.request("GET", BASE_URL, params=search_query_fields)
    return response


@pytest.fixture(params=url)
def search_query_human_readable():
    """Get request with search query params in human readable format"""
    response = requests.request("GET", BASE_URL, params=url)
    return response


# @pytest.fixture()
def base_url():
    """Return base API url"""
    return BASE_URL


# @pytest.fixture(params=querystring)
def human_output():
    """Get request with human output params"""
    response = requests.request("GET", BASE_URL, params=querystring)
    return response


@pytest.fixture(params=query)
def search_query():
    """Get request with search query params"""
    response = requests.request("GET", BASE_URL, params=query)
    return response


@pytest.fixture(params=fieldstring)
def fields():
    """Get request with fields params"""
    response = requests.request("GET", BASE_URL + '/jquery', params=fieldstring)
    return response

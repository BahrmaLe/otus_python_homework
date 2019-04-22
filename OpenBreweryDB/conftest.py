"""Fixtures for tests.py """
import pytest

BASE_URL = 'https://api.openbrewerydb.org'


@pytest.fixture
def base_url():
    """Return base API url"""
    return BASE_URL

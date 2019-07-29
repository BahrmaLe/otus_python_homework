"""Fixtures for Socket tests and HTM parser"""
import pytest


def pytest_addoption(parser):
    """Get commands for teminal"""
    parser.addoption('--server', default="192.168.56.103", action="store", help='Specify server')
    parser.addoption('--method',  default="GET /opencart/ ", action="store", help='Specify method')
    parser.addoption('--header',  default="Date", action='store', help='Specify header')
    parser.addoption('--port',  default=80, action="store", help='Specify port')
    parser.addoption('--images',  default=False, action="store_true", help='Show images')
    parser.addoption('--links',  default=False, action="store_true", help='Show links')
    parser.addoption('--tags',  default=False, action="store_true", help='Show tags')
    parser.addoption('--toptag',  default=False, action="store_true", help='Show the most frequent tag')


@pytest.fixture(autouse=True)
def server(request):
    return request.config.getoption("--server")


@pytest.fixture(autouse=True)
def method(request):
    return request.config.getoption("--method")


@pytest.fixture(autouse=True)
def header(request):
    return request.config.getoption("--header")


@pytest.fixture(autouse=True)
def port(request):
    return request.config.getoption("--port")


"""Fixtures for tests.py (Dogs API testing)"""
import pytest
import requests


URLS = ["https://dog.ceo/dog-api/",
        "https://dog.ceo/api/breeds/list/all",
        "https://dog.ceo/api/breeds/image/random",
        "https://dog.ceo/api/breeds/image/random/3",
        "https://dog.ceo/api/breed/hound/images",
        "https://dog.ceo/api/breed/hound/images/random",
        "https://dog.ceo/api/breed/hound/images/random/3",
        "https://dog.ceo/api/breed/hound/list",
        "https://dog.ceo/api/breed/hound/afghan/images",
        "https://dog.ceo/api/breed/hound/afghan/images/random",
        "https://dog.ceo/api/breed/hound/afghan/images/random/3", ]
"""List general ULRS with Dogs API"""
HEADERS = [{"Content-type": "application/json"}, {"Content-type": "text/html"}, {}]
PAIRS = [(url, header) for url in URLS for header in HEADERS]


@pytest.fixture(params=PAIRS)
def pairs_of_response(request):
    """pairwise testing for content-type, headers in responses for all urls """
    response = requests.get(request.param[0], headers=request.param[1])
    print(request.param[0])
    print(request.param[1])
    return response


@pytest.fixture()
def listallbreeds():
    """GET Request to https://dog.ceo/api/breeds/list/all and return Json data"""
    response = requests.get(URLS[1])
    json_data = response.json()
    return json_data


@pytest.fixture()
def randomimage():
    """GET Request to "https://dog.ceo/api/breeds/image/random/3"
    and return Json data with random image"""
    class Randomimage():
        """"I don't know why it here, I am google it"""
        @staticmethod
        def get_random_image():
            """Function for class"""
            response = requests.get(URLS[2])
            json_data = response.json()
            return json_data

    return Randomimage()


@pytest.fixture()
def randomthreeimage():
    """GET Request to "https://dog.ceo/api/breeds/image/random"
    and return Json data with three random image"""
    class Randomimage():
        """"I don't know why it here, I am google it"""
        @staticmethod
        def get_random_three_image():
            """Function for class"""
            response = requests.get(URLS[3])
            json_data = response.json()
            return json_data

    return Randomimage()


@pytest.fixture()
def list_of_breed():
    """GET Request to "https://dog.ceo/api/breed/hound/images"
    and return Json data with list а all images by breed
    "hound" """
    response = requests.get(URLS[4])
    json_data = response.json()
    return json_data


@pytest.fixture()
def get_random_image_by_breed():
    """GET Request to "https://dog.ceo/api/breed/hound/images/random"
    and return Json data with random image by breed"""
    class Randomimage():
        """"I don't know why it here, I am google it"""
        @staticmethod
        def get_random_image():
            """Function for class"""
            response = requests.get(URLS[5])
            json_data = response.json()
            return json_data

    return Randomimage()


@pytest.fixture()
def get_random_three_image_by_breed():
    """GET Request to "https://dog.ceo/api/breed/hound/images/random/3"
    and return Json data with random three image
    by breed """
    class Randomimage():
        """"I don't know why it here, I am google it"""
        @staticmethod
        def get_random_three_image():
            """Function for class"""
            response = requests.get(URLS[6])
            json_data = response.json()
            return json_data

    return Randomimage()


@pytest.fixture()
def listallsubbreeds():
    """GET Request to "https://dog.ceo/api/breed/hound/images"
    and return Json data with list а all images by sub-breeds
    for "hound" """
    response = requests.get(URLS[7])
    json_data = response.json()
    return json_data


@pytest.fixture()
def list_of_subbreed():
    """GET Request to "https://dog.ceo/api/breed/hound/afghan/images"
    and return Json data with list а all images by
    sub-breed "afghan" """
    response = requests.get(URLS[8])
    json_data = response.json()
    return json_data


@pytest.fixture()
def get_random_image_by_subbreed():
    """GET Request to "https://dog.ceo/api/breed/hound/afghan/images/random"
    and return Json data with random image
    by sub-breed "afghan" """
    class Randomimage():
        """"I don't know why it here, I am google it"""
        @staticmethod
        def get_random_image():
            """Function for class"""
            response = requests.get(URLS[9])
            json_data = response.json()
            return json_data

    return Randomimage()


@pytest.fixture()
def get_random_three_image_by_subbreed():
    """GET Request to "https://dog.ceo/api/breed/hound/afghan/images/random/3"
    and return Json data with three random
    image by sub-breed "afghan" """
    class Randomimage():
        """"I don't know why it here, I am google it"""
        @staticmethod
        def get_random_three_image():
            """Function for class"""
            response = requests.get(URLS[10])
            json_data = response.json()
            return json_data

    return Randomimage()

"""Test for Dogs API """
import pytest


@pytest.mark.usefixtures("pairs_of_response")
def test_urls(pairs_of_response):
    """pairwise testing for content-type, headers in responses for all urls """
    print(type(pairs_of_response.status_code))
    assert pairs_of_response.status_code == 200


def test_list_all_breeds(listallbreeds):
    """Test status, type and content for list of all breeds"""
    print(listallbreeds)
    print(type(listallbreeds['message']))
    assert 'status' in listallbreeds
    assert 'success' in listallbreeds['status']
    assert 'message' in listallbreeds
    assert type(listallbreeds['message']) is dict


def test_random_image(randomimage):
    """Test that returns random image"""
    a = randomimage.get_random_image()
    b = randomimage.get_random_image()
    print(a)
    print(b)
    assert a != b


def test_random_three_image(randomthreeimage):
    """Test that returns random three images list"""
    a = randomthreeimage.get_random_three_image()
    b = randomthreeimage.get_random_three_image()
    print(a)
    print(b)
    assert a != b


def test_images_by_breed(list_of_breed):
    """Test that returns images for breed "hound" """
    print(len(list_of_breed['message']))
    for i in (list_of_breed['message']):
        assert 'hound' in i
    assert 'success' in list_of_breed['status']
    assert 'message' in list_of_breed
    assert type(list_of_breed['message']) is list


def test_random_image_by_breed(get_random_image_by_breed):
    """Test that returns random image for breed "hound" """
    a = get_random_image_by_breed.get_random_image()
    b = get_random_image_by_breed.get_random_image()
    print(a)
    print(b)
    assert a != b
    assert 'hound' in a['message']
    assert 'hound' in b['message']


def test_random_three_image_by_breed(get_random_three_image_by_breed):
    """Test that returns random three images for breed "hound" """
    a = get_random_three_image_by_breed.get_random_three_image()
    b = get_random_three_image_by_breed.get_random_three_image()
    print(a)
    print(b)
    print(len(a['message']))
    print(len(b['message']))
    assert a != b
    for i in (a['message']):
        assert 'hound' in i
    for i in (b['message']):
        assert 'hound' in i


def test_list_all_subbreeds(listallsubbreeds):
    """Test that returns list all subbreeds"""
    print(listallsubbreeds)
    print(len(listallsubbreeds['message']))
    assert 'status' in listallsubbreeds
    assert 'success' in listallsubbreeds['status']
    assert 'message' in listallsubbreeds
    assert type(listallsubbreeds['message']) is list


def test_images_by_subbreed(list_of_subbreed):
    """Test that returns image for subbreed"""
    print(len(list_of_subbreed['message']))
    for i in (list_of_subbreed['message']):
        assert 'afghan' in i
    assert 'success' in list_of_subbreed['status']
    assert 'message' in list_of_subbreed
    assert type(list_of_subbreed['message']) is list


def test_random_image_by_subbreed(get_random_image_by_subbreed):
    """Test that returns random image for subbreed"""
    a = get_random_image_by_subbreed.get_random_image()
    b = get_random_image_by_subbreed.get_random_image()
    print(a)
    print(b)
    assert a != b
    assert 'afghan' in a['message']
    assert 'afghan' in b['message']


def test_random_three_image_by_subbreed(get_random_three_image_by_subbreed):
    """Test that returns three random image for subbreed"""
    a = get_random_three_image_by_subbreed.get_random_three_image()
    b = get_random_three_image_by_subbreed.get_random_three_image()
    print(a)
    print(b)
    print(len(a['message']))
    print(len(b['message']))
    assert a != b
    for i in (a['message']):
        assert 'afghan' in i
    for i in (b['message']):
        assert 'afghan' in i

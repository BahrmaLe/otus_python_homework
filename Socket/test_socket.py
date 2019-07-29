"""Tests socket connection"""
from Socket.requests import Requests


def test_socket(request, header):
    """Test socket session with getting headers"""
    d = Requests(request)
    print(d.headers())
    print(d.get_status_code())
    assert d.get_status_code() == 200
    if header:
        try:
            print(d.headers()[header])
        except KeyError:
            print("No headers")




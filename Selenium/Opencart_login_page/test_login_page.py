def test_login(current_url):
    """Test correctly login and check admin url"""
    print(current_url)
    assert "dashboard" in current_url

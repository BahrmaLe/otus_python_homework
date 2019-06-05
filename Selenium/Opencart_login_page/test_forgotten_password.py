def test_forgotten_password(forgot_link):
    """Test redirection to forgot password page"""
    print(forgot_link)
    assert "forgotten" in forgot_link

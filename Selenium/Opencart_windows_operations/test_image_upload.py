"""Tests for products page"""


@pytest.mark.usefixtures("add_product")
def test_products(products_list):
    """Test that New product is added"""
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '1.JPG')
    input_manager = chrome_browser.find_element_by_css_selector('input.upload1')
    input_manager.send_keys(filename)
    assert "New Product" in products_list

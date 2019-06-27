"""Tests for products page"""
import pytest


# @pytest.fixture(scope='function')
# @pytest.mark.usefixtures("login_action", "open_products_page")
# def add_product(driver, products_page, product_card):
#     """Adding new product"""
#     products_page.addnew2()
#     product_card.productname('New Product')
#     product_card.metatag('New Meta Tag Keyword')
#     product_card.datatab()
#     product_card.modelname('New model')
#     product_card.savebutton()
#     driver.back()
#     driver.back()
#     driver.refresh()


@pytest.mark.usefixtures("add_product")
def test_products(products_list):
    """Test that New product is added"""
    assert "New Product" in products_list

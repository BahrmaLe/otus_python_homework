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


@pytest.mark.usefixtures("add_product", "driver", "open_login_page", "login_action", "open_products_page")
def test_products(products_list):
    """Test that New product is added"""
    assert "New Product" in products_list


@pytest.fixture(scope='function')
@pytest.mark.usefixtures("driver", "open_login_page", "login_action", "open_products_page")
def products_list(products_page):
    """Return products list with names"""
    products_page.products_list()


@pytest.fixture(scope='function')
def products_list(driver, open_login_page, login_action, open_products_page):
   """Return products list with names"""
   products = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody')
   products_elements = products.find_elements_by_tag_name("tr")
   product_list = set()
   for element in products_elements:
       product_name = element.find_elements_by_tag_name("td")[2]
       product_list.add(product_name.text)
   print(product_list)
   return product_list
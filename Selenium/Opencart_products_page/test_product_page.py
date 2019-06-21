"""Tests for products page"""
import pytest


@pytest.mark.usefixtures("add_product",
                         "driver",
                         "open_login_page",
                         "login_action",
                         "open_products_page")
def test_products(products_list):
    """Test that New product is added"""
    assert "New Product" in products_list


@pytest.mark.usefixtures("driver",
                         "open_login_page",
                         "login_action",
                         "open_products_page",
                         "edit_product")
def test_edit_product(products_list):
    """Test that New product is edited"""
    assert "Edited Product" in products_list


@pytest.mark.usefixtures("driver",
                         "open_login_page",
                         "login_action",
                         "open_products_page",
                         "delete_product")
def test_delete_product(products_list):
    """Test that product is deleted"""
    assert "Edited Product" not in products_list

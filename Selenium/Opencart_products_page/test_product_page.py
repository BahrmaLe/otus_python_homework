"""Tests for products page"""
import pytest


@pytest.mark.usefixtures("add_product")
def test_products(products_list):
    """Test that New product is added"""
    assert "New Product" in products_list


@pytest.mark.usefixtures("edit_product")
def test_edit_product(products_list):
    """Test that New product is edited"""
    assert "New Product Edited" in products_list


@pytest.mark.usefixtures("delete_product")
def test_delete_product(products_list):
    """Test that product is deleted"""
    assert "New Product Edited" not in products_list

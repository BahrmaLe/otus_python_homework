"""Tests for products page"""
import os
import sqlite3
import pytest
# import allure


# @allure.title("Add New Product")
# @allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("add_product")
def test_products(products_list):
    """Test that New product is added"""
    # allure.attach(products_list, 'Attach with HTML type', allure.attachment_type.HTML)
    assert "product_id" in products_list

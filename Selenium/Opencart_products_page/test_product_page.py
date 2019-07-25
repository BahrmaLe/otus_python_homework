"""Tests for products page"""
import pytest
import allure


@allure.title("Add New Product")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("add_product")
def test_products(products_list):
    """Test that New product is added"""
    # allure.attach(products_list, 'Attach with HTML type', allure.attachment_type.HTML)
    assert "New Product" in products_list


@allure.title("Edit Product")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("edit_product")
def test_edit_product(products_list):
    """Test that New product is edited"""
    # allure.attach(products_list, 'Attach with HTML type', allure.attachment_type.HTML)
    assert "New Product Edited" in products_list


@pytest.mark.xfail(condition=lambda: True, reason='Need to update Chrome browser')
@allure.title("Delete Product")
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.usefixtures("delete_product")
def test_delete_product(products_list):
    """Test that product is deleted"""
    # allure.attach(products_list, 'Attach with HTML type', allure.attachment_type.HTML)
    assert "New Product Edited" not in products_list



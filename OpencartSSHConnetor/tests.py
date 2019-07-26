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


def test_db():
    """Test DB"""
    dir_path = os.path.dirname(os.path.abspath(__file__))
    print(dir_path)
    base_path = "/".join([dir_path, "log/logs/logs.db"])
    print(base_path)
    # base_path = "C:/Users/60064265/PycharmProjects/Homework/Selenium/Opencart_products_page/db/logs.db"
    conn = sqlite3.connect(base_path)
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM log ")
    for rows in result:
        print(rows)

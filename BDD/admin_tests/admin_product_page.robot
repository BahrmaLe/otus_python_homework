*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource_1.robot

*** Test Cases ***
Valid Add Product
    Remove old DB if exists
    Connect to SQLiteDB
    Create Product table
    Open Browser To Local Admin Page
    Input Username    admin
    Input Password    admin
    Submit Admin
    Product Should Be Added    !!!AAA
    Table Must Exist - product
    Execute SQL Script - Insert Data product table
    [Teardown]    Close Browser

Valid Delete Product
    Connect to SQLiteDB
    Open Browser To Local Admin Page
    Input Username    admin
    Input Password    admin
    Submit Admin
    Product Should Be Deleted
    Table Must Exist - product
    Execute SQL Script - Insert Data product table
    [Teardown]    Close Browser





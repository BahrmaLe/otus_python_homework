*** Settings ***
Suite Setup      Remove old DB if exists
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource_1.robot

*** Test Cases ***
Valid Add Product
    Open Browser To Local Admin Page
    Input Username    admin
    Input Password    admin
    Submit Admin
    Product Should Be Added    !!!AAA
    Connect to SQLiteDB
    Create Product table
    Table Must Exist - product
    Execute SQL Script - Insert Data product table
    [Teardown]    Close Browser

#Valid Delete Product
#    Open Browser To Local Admin Page
#    Input Username    admin
#    Input Password    admin
#    Submit Admin
#    Product Should Be Deleted
#    Execute SQL Script - Insert Data product table
#    [Teardown]    Close Browser





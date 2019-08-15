*** Settings ***
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
    [Teardown]    Close Browser

Valid Delete Product
    Open Browser To Local Admin Page
    Input Username    admin
    Input Password    admin
    Submit Admin
    Product Should Be Deleted
    [Teardown]    Close Browser



#Valid Delete Product
#    Open Browser To Login Page
#    Input Username    Admin
#    Input Password    Admin
#    Submit Credentials
#    Сustommenu Page Should Be Open
#    [Teardown]    Close Browser
#
#Valid Count Products
#    Open Browser To Login Page
#    Input Username    Admin
#    Input Password    Admin
#    Submit Credentials
#    Setting Page Should Be Open
#    [Teardown]    Close Browser

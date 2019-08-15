*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    demo
    Input Password    demo
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser

Valid Category page
    Open Browser To Login Page
    Input Username    demo
    Input Password    demo
    Submit Credentials
    Category Page Should Be Open
    [Teardown]    Close Browser

Valid Custommenu page
    Open Browser To Login Page
    Input Username    demo
    Input Password    demo
    Submit Credentials
    Сustommenu Page Should Be Open
    [Teardown]    Close Browser

Valid Setting page
    Open Browser To Login Page
    Input Username    demo
    Input Password    demo
    Submit Credentials
    Setting Page Should Be Open
    [Teardown]    Close Browser

Valid Report page
    Open Browser To Login Page
    Input Username    demo
    Input Password    demo
    Submit Credentials
    Report Page Should Be Open
    [Teardown]    Close Browser
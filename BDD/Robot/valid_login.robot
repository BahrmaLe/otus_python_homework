*** Settings ***
Library          Selenium2Library     implicit_wait=5.0
Library          ActionClass.py

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username
    Input Password
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser
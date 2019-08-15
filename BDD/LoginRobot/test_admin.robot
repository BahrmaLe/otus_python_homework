*** Settings ***
Documentation    Test suite for test login as admin and customer in OpenCart
Library          Selenium2Library     implicit_wait=10.0
Library          Login.py
*** Test Cases ***
Admin Login
    Login Admin
    Admin page is opened

#Open Category Menu
#    Open Category
#    Category Page is opened
#
#Open Design Menu
#    Open Menu Designer
#    Menu Designer is opened
#
#Open System Settings
#    Open Settings
#    Settings is opened
#
#Open Reports
#    Open orders
#    Orders is opened

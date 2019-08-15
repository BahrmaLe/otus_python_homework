*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${SERVER}         demo23.opencart.pro
${LOCAL SERVER}         192.168.56.103/opencart
${BROWSER}        Chrome
${DELAY}          0
${VALID USER}     demo
${VALID PASSWORD}    demo
${LOGIN URL}      http://${SERVER}/admin/
${WELCOME URL}    http://${SERVER}/welcome.html
${ERROR URL}      http://${SERVER}/error.html
${LOCAL ADMIN URL}      http://${LOCAL SERVER}/admin/
${DASHBOARD}      dashboard
${CATEGORY}      category
${CUSTOMMENU}      custommenu
${SETTING}      setting
${REPORT}      report
${Count}

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be    Авторизация

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    css=#input-username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    css=#input-password    ${password}

Submit Credentials
    Click Button    css=#content > div > div > div > div > div.panel-body > form > div.text-right > button

Welcome Page Should Be Open
    Location Should Contain    ${DASHBOARD}
    Title Should Be    Панель состояния

Category Page Should Be Open
    Click Element    xpath=//*[@id="button-menu"]
    Element Should Be Visible    xpath=//*[@id="menu-catalog"]/a
    Click Element    xpath=//*[@id="menu-catalog"]/a
    Element Should Be Visible    css=#menu-catalog > ul > li:nth-child(1) > a
    Click Element    css=#menu-catalog > ul > li:nth-child(1) > a
    Location Should Contain    ${CATEGORY}
    Title Should Be    Категории

Сustommenu Page Should Be Open
    Click Element    xpath=//*[@id="button-menu"]
    Element Should Be Visible    css=#menu-design > a
    Click Element    xpath=//*[@id="menu-design"]/a
    Wait Until Element Is Visible    xpath=//*[@id="menu-design"]/ul/li[2]/a
    Click Element    xpath=//*[@id="menu-design"]/ul/li[2]/a
    Location Should Contain    ${CUSTOMMENU}
    Title Should Be    Конструктор Меню

Setting Page Should Be Open
    Click Element    xpath=//*[@id="button-menu"]
    Element Should Be Visible    css=#menu-system > a > span
    Click Element    css=#menu-system > a > span
    Element Should Be Visible    xpath=//*[@id="menu-system"]/ul/li[1]/a
    Click Element    xpath=//*[@id="menu-system"]/ul/li[1]/a
    Location Should Contain    ${SETTING}
    Title Should Be    Магазины

Report Page Should Be Open
    Click Element    xpath=//*[@id="button-menu"]
    Element Should Be Visible    css=#menu-report > a > span
    Click Element    css=#menu-report > a > span
    Element Should Be Visible    xpath=//*[@id="menu-report"]/ul/li[1]/a
    Click Element    xpath=//*[@id="menu-report"]/ul/li[1]/a
    Element Should Be Visible    xpath=//*[@id="menu-report"]/ul/li[1]/ul/li[1]/a
    Click Element    xpath=//*[@id="menu-report"]/ul/li[1]/ul/li[1]/a
    Location Should Contain    ${REPORT}
    Title Should Be    Отчет по продажам

Open Browser To Local Admin Page
    Open Browser    ${LOCAL ADMIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Submit Admin
    Click Button    xpath=//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button

Product Should Be Added
    [Arguments]    ${product_name}
    Click Element    xpath=//*[@id="menu-catalog"]/a
    Capture Page Screenshot
    Wait Until Element Is Visible    xpath=//*[@id="collapse1"]/li[2]/a
    Capture Page Screenshot
    Click Element    xpath=//*[@id="collapse1"]/li[2]/a
    Capture Page Screenshot
    ${count1} =     Get Element Count    xpath=//*[@id="form-product"]/div/table/tbody/tr
    Element Should Be Visible    xpath=//*[@id="content"]/div[1]/div/div/a
    Capture Page Screenshot
    Click Element    xpath=//*[@id="content"]/div[1]/div/div/a
    Capture Page Screenshot
    Input Text    xpath=//*[@id="input-name1"]    ${product_name}
    Capture Page Screenshot
    Input Text    xpath=//*[@id="input-meta-title1"]    ${product_name}
    Capture Page Screenshot
    Click Element    xpath=//*[@id="form-product"]/ul/li[2]/a
    Capture Page Screenshot
    Input Text    xpath=//*[@id="input-model"]    ${product_name}
    Capture Page Screenshot
    Click Element    css=#content > div.page-header > div > div > button
    Go Back
    Go Back
    Reload Page
    ${count2} =     Get Element Count    xpath=//*[@id="form-product"]/div/table/tbody/tr
    Should Be True    ${count1}<${count2}
    Capture Page Screenshot

Product Should Be Deleted
    Click Element    xpath=//*[@id="menu-catalog"]/a
    Capture Page Screenshot
    Wait Until Element Is Visible    xpath=//*[@id="collapse1"]/li[2]/a
    Capture Page Screenshot
    Click Element    xpath=//*[@id="collapse1"]/li[2]/a
    Capture Page Screenshot
    ${count1} =     Get Element Count    xpath=//*[@id="form-product"]/div/table/tbody/tr
    Capture Page Screenshot
    Select Checkbox    xpath=//*[@id="form-product"]/div/table/tbody/tr[1]/td[1]/input
    Capture Page Screenshot
    Select Checkbox    xpath=//*[@id="form-product"]/div/table/tbody/tr[2]/td[1]/input
    Capture Page Screenshot
    Choose Ok On Next Confirmation
    Click Element    css=#content > div.page-header > div > div > button.btn.btn-danger
    Confirm Action
    ${count2} =     Get Element Count    xpath=//*[@id="form-product"]/div/table/tbody/tr
    Should Be True    ${count1}>${count2}
    Capture Page Screenshot


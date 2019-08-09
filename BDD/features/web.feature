@web @opencart
Feature: Opencart Web Browsing
  As a client,
  I want to find product on opencart,
  So I can buy product from opencart shop.

  Background:
    Given the Opencart home page is displayed

  Scenario: Basic Opencart Search
    When the user searches for "Mac"
    Then results are shown for "Mac"

  Scenario: Open Openacart Product page
    When the user click on Product
    Then Product page is opened

  Scenario: Add to Card Openacart Product
    When the user click on Add to Cart
    Then Product appears in user cart

  Scenario: Remove from cart Openacart Product
    When the user click on Remove
    Then Product removed from user cart

  Scenario: Back to Home Openacart page
    When the user click on Home page
    Then Home page is opened

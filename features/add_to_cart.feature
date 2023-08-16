Feature: Add To Cart
As a user, I want to buy some products on your site

  @addToCardUsingValidAccount
  Scenario Outline: Should Buy Product By Using The Valid Account
    Given I navigate to Wizeline page
    And I login by using <userName> username and <password> password
    And I navigate to Product page
    When I choose <product> product to add to cart
    And I navigate to Cart page
    And <product> product is available on Cart page
    And I checkout on Cart page
    And I navigate to Checkout page
    When I enter <firstName> first name and <lastName> last name and <postalCode> postal code
    Then I navigate to Overview page

    Examples:
      | userName        | password       | product             | firstName | lastName | postalCode |
      | "standard_user" | "secret_sauce" | "Sauce Labs Onesie" | "Hung"    | "Nguyen" | "084"      | 
  
Feature: Login
As a user, I want to login to your site

  @loginWithValidAccount
  Scenario Outline: Should Login With The Standard Account
    Given I navigate to Wizeline page
    When I login by using <username> username and <password> password
    Then I navigate to Product page

    Examples:
      | username                   | password       | 
      | "standard_user"            | "secret_sauce" |
      | "performance_glitch_user"  | "secret_sauce" |

  @loginWithLockedAccount
  Scenario Outline: Should Not Login With The Locked Account
    Given I navigate to Wizeline page
    When I login by using <username> username and <password> password
    Then I can see this <error> error message

    Examples:
      | username          | password       | error                                                 |  
      | "locked_out_user" | "secret_sauce" | "Epic sadface: Sorry, this user has been locked out." |
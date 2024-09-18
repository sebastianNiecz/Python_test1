Feature: Test1


  Scenario Outline: Successfully find button on the specified page
    Given I am a user on the specified "<page>" page
    When I should see search button
    And I should see name of the button "<name>"
    And I set name "<company_name>" in search element input
    And I click search button
    Then I should see found page name "<page_name>"

  Examples:
    | page                  | name            | company_name | page_name              |
    | https://www.google.pl | Szukaj w google | energotest   | www.spie-energotest.pl |
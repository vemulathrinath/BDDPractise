# Created by Thrinath at 21-04-2024
  # Enter feature name here
Feature: Search feature
  # Enter feature description here

  # Enter scenario name here
  Scenario: Validating the google search feature
    # Enter steps here
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text to search
    And I click the search button
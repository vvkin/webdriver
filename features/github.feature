Feature: GitHub search
  As a regular GitHub user
  I want to search for the repository
  And to get key information about it

  Scenario Outline: Search for <query> repository
    Given I open the GitHub website
    When I enter the <query> repository
    Then I am being redirected to the page with <query> results
    And repositories number is greater than null
    And the related topic is <topic>
    And the first repository is <repository>
    And its language is <language>
    And <language> is present within related languages

  Examples: Queries
    | query          | topic         | repository          | language   |
    | torvalds/linux | Linux         | torvalds/linux      | C          |
    | react          | React         | facebook/react      | JavaScript |
    | alacritty      | Not specified | alacritty/alacritty | Rust       |

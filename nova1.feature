# Created by meih0 at 10/17/2019
Feature: NOVA Job Center

  Scenario: Search for "automation" job on job board
    Given Go to link "Search for an open job"
    Then Locate "keywords" field and enter "automation"
    Then Click button "Find Jobs"
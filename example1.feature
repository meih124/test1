# Created by meih0 at 10/30/2019
Feature: Example.com

  Scenario: Assert text of h1 title
    Given Go to URL "http://www.example.com"
    Then Assert tag "h1" text displayed is "Example Domain"
    Then Go to link "More information"

  Scenario: Click on top nav bar links
    Given Go to URL "https://www.iana.org/domains/reserved"
    Then Click "navigation" link "Domains"
    Then Assert URL is "https://www.iana.org/domains"
    Then Click "navigation" link "Numbers"
    Then Assert URL is "https://www.iana.org/numbers"
    Then Click "navigation" link "About Us"
    Then Assert URL is "https://www.iana.org/about"

  Scenario: Click on side bar links
    Given Go to URL "https://www.iana.org/domains/reserved"
    Then Click "navigation" link "Protocols"
    Then Assert URL is "https://www.iana.org/protocols"
    Then Click "navigation_box" link "Time Zone Database"
    Then Assert URL is "https://www.iana.org/time-zones"
    Then Click "navigation_box" link "Performance"
    Then Assert URL is "https://www.iana.org/performance/ietf-statistics"
    Then Click "navigation_box" link "IETF Draft Status"
    Then Assert URL is "https://www.iana.org/performance/ietf-draft-status"
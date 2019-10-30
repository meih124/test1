# Created by meih0 at 10/30/2019
Feature: Testing the-internet.herokuapp.com pages

  Scenario: Basic Auth
    Given Go to URL "http://the-internet.herokuapp.com/"
    Then Auth directly through URL

  Scenario: Type in Iframe window
    Given Go to URL "http://the-internet.herokuapp.com/"
    Then Go to link "Frames"
    Then Go to link "iFrame"
    Then Type "Hello world" in Iframe
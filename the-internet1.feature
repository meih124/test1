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

  Scenario: Click 3rd edit button
    Given Go to URL "http://the-internet.herokuapp.com/"
    Then Go to link "Challenging DOM"
    Then Click specific edit button
    Then Assert URL is "http://the-internet.herokuapp.com/challenging_dom#edit"

  Scenario: Click appearing button
    Given Go to URL "http://the-internet.herokuapp.com/"
    Then Go to link "Disappearing Elements"
    Then Click appearing button "Gallery"
    Then Assert URL is "http://the-internet.herokuapp.com/gallery/"

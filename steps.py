from lettuce import step, world
import verify
from verify import expect


@step('Go to URL "([^"]*)"')
def open_page(step, url):
    world.driver.get(url)


@step('Go to link "([^"]*)"')
def open_link(step, link_text):
    link_name = world.driver.find_element_by_partial_link_text(link_text)
    link_name.click()


@step('Locate "([^"]*)" field and enter "([^"]*)"')
def find_field(step, field_id, keyword_text):
    field = world.driver.find_element_by_id(field_id)
    field.send_keys(keyword_text)


@step('Click button "([^"]*)"')
def click_button(step, button_text):
    button = world.driver.find_element_by_xpath("//button[@type='submit'][text()='%s']" %button_text)
    button.click()


@step('Assert tag "([^"]*)" text displayed is "([^"]*)"')
def assert_text(step, tag_name, displayed_text):
    element = world.driver.find_element_by_tag_name('%s' %tag_name)
    assert element.text == displayed_text, ("Displayed text unexpectedly shows '%s' instead of '%s'" %(element.text, displayed_text))


@step('Click "([^"]*)" link "([^"]*)"')
def click_side_nav_link(step, location, link_name):
    link_name = world.driver.find_element_by_xpath("//div[@class='%s']/ul/li/a[@href][text()='%s']" %(location, link_name))
    link_name.click()


@step('Assert URL is "([^"]*)"')
def assert_url(step, displayed_text):
    assert world.driver.current_url == displayed_text, ("Displayed text unexpectedly shows '%s' instead of '%s'" %(current_url, displayed_text))



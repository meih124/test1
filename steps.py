from lettuce import step, world
from selenium.common.exceptions import NoSuchElementException
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


@step('Auth directly through URL')
def auth_thru_url(step):
    world.driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')


@step('Type "([^"]*)" in Iframe')
def input_text_iframe(step, input_text):
    world.driver.switch_to.frame('mce_0_ifr')
    editor = world.driver.find_element_by_id('tinymce')
    editor.clear()
    editor.send_keys(input_text)


@step('Click specific edit button')
def click_edit_button(step):
    button = world.driver.find_element_by_xpath("//td[text()='Phaedrum2']/following-sibling::td/a[text()='edit']")
    button.click()


@step('Click appearing button "([^"]*)"')
def click_visible_button(step, button_text):
    while True:
        try:
            world.driver.find_element_by_xpath("//a[text()='%s']" %button_text)
        except NoSuchElementException:
            world.driver.refresh()
        else:
            world.driver.find_element_by_xpath("//a[text()='%s']" % button_text).click()
            break
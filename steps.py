from lettuce import step, world


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


@step('Assert text displayed is "([^"]*)"')
def assert_text(step, displayed_text):
    element = world.driver.find_element_by_tag_name('h1')
    assert element.text == displayed_text
    # if element.text != displayed_text:
    #     raise ValueError("Displayed text should be '%s''" %displayed_text)

from selenium import webdriver
from lettuce import *


@before.all
def open_browser():
    world.driver = webdriver.Chrome()
    world.driver.maximize_window()
    world.driver.get('http://www.google.com')
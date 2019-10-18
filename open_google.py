from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.google.com')
driver.quit()
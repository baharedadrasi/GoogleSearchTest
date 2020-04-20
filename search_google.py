from selenium import webdriver
from Google import GoogleHomePage


driver = webdriver.Chrome()
driver.get('https://www.google.com')
page = GoogleHomePage(driver)

page.query('python')
page.search()
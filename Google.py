from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class GoogleHomePage:

    def __init__(self, driver):
        self.driver = driver

    def query(self, text):
        elem = self.driver.find_element_by_css_selector('input[name="q"]')
        elem.send_keys(text)

    def search(self):
        elem = self.driver.find_element_by_css_selector('input[name="q"]')
        elem.send_keys(Keys.RETURN)

    
        

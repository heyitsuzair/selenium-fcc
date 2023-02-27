from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get('http://webdriveruniversity.com/Click-Buttons/index.html')
driver.implicitly_wait(3)
my_element = driver.find_element('id', 'button1')
my_element.click()

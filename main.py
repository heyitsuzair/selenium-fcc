from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get('https://webdriveruniversity.com/Contact-Us/contactus.html')

fname = driver.find_element(By.NAME, 'first_name')
lname = driver.find_element(By.NAME, 'last_name')
email = driver.find_element(By.NAME, 'email')
message = driver.find_element(By.NAME, 'message')
reset = driver.find_elements(
    By.CSS_SELECTOR, "input[class='contact_button']")[0]
submit = driver.find_elements(
    By.CSS_SELECTOR, "input[class='contact_button']")[1]

fname.send_keys('Muhammad')
lname.send_keys('Uzair')
email.send_keys('uzair@gmail.com')

for i in range(3):
    message.send_keys(Keys.SHIFT)
    message.send_keys(Keys.ENTER)
submit.click()

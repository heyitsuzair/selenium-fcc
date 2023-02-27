from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get('http://webdriveruniversity.com/Click-Buttons/index.html')
driver.implicitly_wait(8)
my_element = driver.find_element('id', 'button1')
my_element.click()


WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'modal-title'),
        'Congratulations!'
    )
)

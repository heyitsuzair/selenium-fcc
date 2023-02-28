from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):

        for star_value in star_values:
            star_box = self.driver.find_element(
                By.CSS_SELECTOR, f'div[data-filters-item="class:class={star_value}"]')
            star_box.click()
    
    def apply_sort(self):
        price_box = self.driver.find_element(
                By.CSS_SELECTOR, f'input[name="pri=1"]')
        price_box.click()
        time.sleep(50)

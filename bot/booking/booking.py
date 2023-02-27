from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.by import By
import time


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r'C:\SeleniumDriver'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()

        currency_btn = self.find_elements(
            By.CLASS_NAME, 'ea1163d21f')

        try:
            close_modal = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')

            close_modal.click()
        except:
            return False

        for btn in currency_btn:
            try:
                if btn.text == currency:
                    btn.click()
            except:
                return False

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':Ra9:')
        search_field.clear()
        search_field.send_keys(place_to_go)
        
        autocomp_results=self.find_elements(By.CSS_SELECTOR,'div[data-testid="autocomplete-result"]')
        autocomp_results[0].click()
        time.sleep(10)

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

        for btn in currency_btn:
            try:
                if btn.text == currency:
                    btn.click()
            except:
                return False

    def close_modal(self):
        try:
            close_modal = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')

            close_modal.click()
        except:
            return False

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':Ra9:')
        search_field.clear()
        search_field.send_keys(place_to_go)

        autocomp_results = self.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="autocomplete-result"]')
        autocomp_results[0].click()

    def select_dates(self, check_out_date, check_in_date):
        check_in = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_in.click()
        check_out = self.find_element(
            By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        check_out.click()

    def select_occupancy(self, no_of_adults):
        adults_elem = self.find_element(
            By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        adults_elem.click()

        adult_value = self.find_element(By.CLASS_NAME, 'e615eb5e43')
        decrease_adult = self.find_element(
            By.CSS_SELECTOR, 'div.e98c626f34>button:first-child')
        increase_adult = self.find_element(
            By.CSS_SELECTOR, 'div.e98c626f34>button:last-child')

        while True:
            decrease_adult.click()

            if adult_value.text == '1':
                print('true')
                break

        for _ in range(no_of_adults - 1):
            increase_adult.click()

    def search(self):
        search_btn = self.find_element(
            By.CSS_SELECTOR, 'button[type=submit]')
        search_btn.click()
        # time.sleep(10)

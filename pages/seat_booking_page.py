from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SeatBookingPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    dep_place_selection = (By.XPATH, '//button[@id="seat-23F"]')
    next_flight = (By.XPATH, '//button[text()=" Наступний рейс "]')
    ret_place_selection = (By.XPATH, '//button[@id="seat-22A"]')
    continue_button = (By.XPATH, '//button[text()=" Продовжити "]')
    fast_track_refuse_locator = (By.XPATH, '//button[text()=" Ні, дякую "]')
    places_locator = (By.XPATH, '//span[text()="Місця"]')

    def place_for_departure_flight_select(self):
        place = self.wait_for_element_is_clickable(*self.dep_place_selection)
        place.click()

    def next_flight_click(self):
        next_flight = self.wait_for_element_is_clickable(*self.next_flight)
        next_flight.click()

    def place_for_return_flight_select(self):
        place = self.wait_for_element_is_clickable(*self.ret_place_selection)
        place.click()

    def continue_button_click(self):
        button = self.wait_for_element_is_clickable(*self.continue_button)
        button.click()

    def refuse_from_the_fast_track(self):
        fast_track = self.wait_for_element_is_clickable(*self.fast_track_refuse_locator)
        fast_track.click()

    def places_selection_completed(self):
        places = self.wait_for_element(*self.places_locator)
        return places.is_displayed()


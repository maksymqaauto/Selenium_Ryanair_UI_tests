from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LuggageBookingPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    add_item_hand_luggage_locator = (By.XPATH, '//label[@for="ry-radio-button--1"]')
    add_luggage_locator = (By.XPATH, '//ry-counter-button[@iconid="glyphs/plus-circle"]')
    continue_button_locator = (By.XPATH, '//button[@data-ref="bags-continue-button"]')
    luggage_locator = (By.XPATH, '//span[text()="Багаж"]')

    def add_one_more_hand_luggage(self):
        element = self.wait_for_element_is_clickable(*self.add_item_hand_luggage_locator)
        element.click()

    def add_one_more_20kg_luggage(self):
        element = self.wait_for_element_is_clickable(*self.add_luggage_locator)
        element.click()

    def click_continue(self):
        element = self.wait_for_element_is_clickable(*self.continue_button_locator)
        element.click()

    def check_luggage_was_added(self):
        element = self.wait_for_element(*self.luggage_locator)
        return element.is_displayed()






from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FlightsInfoPage(BasePage):

    flight_number_locator = '//input[@name="number"]'
    date_field_locator = '//div[@data-ref="input-button__display-value"]'
    date_select_locator = '//div[@data-id="2025-12-13"]'
    search_button_locator = '//button[@aria-label="Пошук"]'
    flight_origin_airport_locator = '//span[@class="flight-info__time__city body-l-lg"]'
    month_select_locator = (By.XPATH, '//div[@data-id="Dec"]')

    def __init__(self, browser):
        super().__init__(browser)

    def set_the_flight_number(self):
        element = self.wait_for_element_is_clickable(By.XPATH, self.flight_number_locator)
        element.click()
        element.clear()
        element.send_keys('7235')

    def set_the_flight_date(self):
        date_field = self.wait_for_element_is_clickable(By.XPATH, self.date_field_locator)
        date_field.click()
        self.switch_to_iframe(1)
        month_to_select = self.wait_for_elements(*self.month_select_locator)[0]
        month_to_select.click()
        date_to_select = self.wait_for_element_is_clickable(By.XPATH, self.date_select_locator)
        date_to_select.click()

    def search_button_click(self):
        button = self.wait_for_element_is_clickable(By.XPATH, self.search_button_locator)
        button.click()

    def check_the_flight_presence(self):
        element = self.wait_for_element(By.XPATH, self.flight_number_locator)
        return element






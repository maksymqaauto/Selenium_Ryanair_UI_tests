from pages.flights_info_page import FlightsInfoPage
from pages.ryanair_page import RyanairPage
import pytest
import allure


@allure.feature('Flight Search')
@allure.story('Search flights')
@pytest.mark.smoke
@pytest.mark.ui
def test_flight_search(driver, flight_search_setup):
    ryanair_page = flight_search_setup
    ryanair_page.set_departure_date()
    ryanair_page.set_return_date()
    ryanair_page.search_button_click()
    assert ryanair_page.wait_for_displaying(), 'The element is absent'


@allure.feature('Flight Search')
@allure.story('Select past date validation')
@pytest.mark.smoke
@pytest.mark.ui
def test_attempt_to_select_past_flight_date(flight_search_setup):
    ryanair_page = flight_search_setup
    assert ryanair_page.past_date_click_check(), 'The date in the past is available for the click'


@allure.feature('Flight Info')
@allure.story('Search flight by number')
@pytest.mark.smoke
@pytest.mark.ui
def test_get_flight_info_by_flight_number(driver):
    ryanair_page = RyanairPage(driver)
    ryanair_page.open()
    ryanair_page.accept_cookie()
    ryanair_page.flights_info_click()
    ryanair_page.switch_to_new_window()
    flights_info_page = FlightsInfoPage(driver)
    flights_info_page.wait_for_dom_ready()
    flights_info_page.set_the_flight_number()
    flights_info_page.set_the_flight_date()
    flights_info_page.search_button_click()
    assert flights_info_page.check_the_flight_presence(), 'The flight has not been found'


@allure.feature('Validation')
@allure.story('Departure and destination check')
@pytest.mark.ui
@pytest.mark.regression
def test_attempt_to_select_the_same_point_for_departure_and_return(driver, ryanair_logged_in):
    ryanair_page = ryanair_logged_in
    ryanair_page.set_departure()
    assert ryanair_page.destination_the_same_as_departure(), 'The same point for departure and destination is available' \
 \
    'for selection'

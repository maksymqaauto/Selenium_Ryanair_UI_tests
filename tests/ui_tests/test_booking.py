import pytest
import allure
from pages.seat_booking_page import SeatBookingPage


@allure.feature('Tariffs')
@allure.story('Select Plus tariff')
@pytest.mark.smoke
@pytest.mark.ui
def test_tariff_plus_selection(driver, flight_search_setup):
    ryanair_page = flight_search_setup
    ryanair_page.month_select()
    ryanair_page.set_dep_date()
    ryanair_page.set_ret_date()
    ryanair_page.search_button_click()
    ryanair_page.set_price_for_departure()
    ryanair_page.set_price_for_return()
    ryanair_page.plus_tariff_select()
    assert ryanair_page.check_that_tariff_was_selected(), 'The tariff plus has not been selected'


@allure.feature('Booking')
@allure.story('Seat booking')
@pytest.mark.smoke
@pytest.mark.ui
def test_seat_booking(driver, ryanair_logged_in):
    ryanair_page = ryanair_logged_in
    ryanair_page.set_departure()
    ryanair_page.set_destination()
    ryanair_page.month_select()
    ryanair_page.set_dep_date()
    ryanair_page.set_ret_date()
    ryanair_page.search_button_click()
    ryanair_page.set_price_for_departure()
    ryanair_page.set_price_for_return()
    ryanair_page.plus_tariff_select()
    ryanair_page.title_selection()
    ryanair_page.name_selection()
    ryanair_page.surname_selection()
    ryanair_page.continue_button_click()
    set_booking_page = SeatBookingPage(driver)
    set_booking_page.place_for_departure_flight_select()
    set_booking_page.next_flight_click()
    set_booking_page.place_for_return_flight_select()
    set_booking_page.continue_button_click()
    set_booking_page.refuse_from_the_fast_track()
    assert set_booking_page.places_selection_completed(), 'The seat booking is not completed'

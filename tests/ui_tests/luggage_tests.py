from pages.luggage_booking_page import LuggageBookingPage
from pages.seat_booking_page import SeatBookingPage
import pytest
import allure


@allure.feature('Booking')
@allure.story('Add luggage')
@pytest.mark.smoke
@pytest.mark.ui
def test_luggage_booking(driver, ryanair_logged_in):
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
    ryanair_page.additional_window_skip()
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
    luggage_booking_page = LuggageBookingPage(driver)
    luggage_booking_page.add_one_more_hand_luggage()
    luggage_booking_page.add_one_more_20kg_luggage()
    luggage_booking_page.click_continue()
    assert luggage_booking_page.check_luggage_was_added(), 'The luggage has not been added'
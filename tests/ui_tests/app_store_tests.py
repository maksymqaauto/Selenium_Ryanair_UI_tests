from pages.app_store_page import AppStorePage
from pages.ryanair_page import RyanairPage
import pytest
import allure


@allure.feature('Integration')
@allure.story('Check app presence in App Store')
@pytest.mark.ui
@pytest.mark.regression
def test_check_the_app_presence_in_apple_store(driver):
    ryanair_page = RyanairPage(driver)
    ryanair_page.open()
    ryanair_page.accept_cookie()
    ryanair_page.apple_store_transition()
    apple_store_page = AppStorePage(driver)
    assert apple_store_page.app_store_url == driver.current_url, "URL mismatch: not on expected App Store page"
    assert apple_store_page.check_name_of_the_app_exists(), "App name not found on the App Store page"

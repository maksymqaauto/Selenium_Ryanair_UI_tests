from pages.ryanair_page import RyanairPage
import pytest
import allure


@allure.feature('UI Settings')
@allure.story('Change language')
@pytest.mark.ui
@pytest.mark.regression
def test_language_change(driver):
    ryanair_page = RyanairPage(driver)
    ryanair_page.open()
    ryanair_page.accept_cookie()
    ryanair_page.language_click()
    ryanair_page.set_us_language()
    assert ryanair_page.check_language_is_english(), 'The language has not been changed'

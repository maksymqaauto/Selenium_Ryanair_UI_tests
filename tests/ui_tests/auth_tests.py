from pages.ryanair_page import RyanairPage
from config.config import invalid_creds
import pytest
import allure


@allure.feature('Authorization')
@allure.story('Valid login')
@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.auth
def test_ryanair_valid_authorization(driver, valid_user_creds):
    ryanair_page = RyanairPage(driver)
    ryanair_page.open()
    ryanair_page.accept_cookie()
    ryanair_page.click_login_link()
    iframe = ryanair_page.wait_for_iframe()
    driver.switch_to.frame(iframe)
    ryanair_page.fill_in_email(valid_user_creds['username'])
    ryanair_page.fill_in_password(valid_user_creds['password'])
    ryanair_page.click_sign_in_button()
    driver.switch_to.default_content()
    assert ryanair_page.check_logout_button_presence(), 'The authorization is failed'


@allure.feature('Authorization')
@allure.story('Invalid login')
@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.parametrize("username, password", invalid_creds)
def test_ryanair_invalid_authorization(driver, username, password):
    ryanair_page = RyanairPage(driver)
    ryanair_page.open()
    ryanair_page.accept_cookie()
    ryanair_page.click_login_link()
    iframe = ryanair_page.wait_for_iframe()
    driver.switch_to.frame(iframe)
    ryanair_page.fill_in_email(username)
    ryanair_page.fill_in_password(password)
    ryanair_page.click_sign_in_button()
    assert ryanair_page.check_alert_msg(), 'The authorization with incorrect credentials proceeded'
    
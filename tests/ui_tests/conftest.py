from selenium import webdriver
import pytest
from config.config import USER_1, PASS_1, USER_2, PASS_2, BASE_URL
from pages.ryanair_page import RyanairPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def valid_user_creds():
    return {"username": USER_1, "password": PASS_1}


@pytest.fixture(scope="session")
def invalid_user_creds():
    return {"username": USER_2, "password": PASS_2}


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def ryanair_logged_in(driver, valid_user_creds):
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
    assert ryanair_page.check_logout_button_presence(), "Login failed"
    return ryanair_page


@pytest.fixture
def flight_search_setup(driver):
    page = RyanairPage(driver)
    page.open()
    page.accept_cookie()
    page.set_departure()
    page.set_destination()
    return page

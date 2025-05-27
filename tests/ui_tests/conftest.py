import os
from datetime import datetime
from selenium import webdriver
from config.config import USER_1, PASS_1, USER_2, PASS_2, BASE_URL
from pages.ryanair_page import RyanairPage
from selenium.webdriver.chrome.service import Service
import logging
import pytest



@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")

    # Используем локально установленный chromedriver из контейнера
    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_file = os.path.join(screenshots_dir, f"{request.node.name}_{timestamp}.png")
        driver.save_screenshot(screenshot_file)

        logs_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, f"{request.node.name}_{timestamp}.log")
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(f"Test '{request.node.name}' failed at {timestamp}\n")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


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


# Настройка логгера один раз
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("logs/pytest.log"),  # путь внутри контейнера, монтируй папку logs в Docker
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def log_test_start_and_finish(request):
    logger.info(f"START test: {request.node.name}")
    yield
    logger.info(f"END test: {request.node.name}")

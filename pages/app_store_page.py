from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config.config import APP_STORE_URL


class AppStorePage(BasePage):
    app_name_locator = '//h1[text()="Ryanair"]'
    app_store_url = APP_STORE_URL

    def __init__(self, browser):
        super().__init__(browser)

    def check_name_of_the_app_exists(self):
        element = self.wait_for_element(By.XPATH, self.app_name_locator)
        return element


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL


class BasePage:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.base_url = BASE_URL
        self.wait = WebDriverWait(browser, timeout)

    def open(self):
        self.browser.get(self.base_url)

    def find_by_xpath(self, xpath_value):
        return self.browser.find_element(By.XPATH, xpath_value)

    def find_by_elements(self, locator):
        return self.browser.find_elements(*locator)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def wait_for_element_is_clickable(self, by, value, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def wait_for_elements(self, by, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located((by, locator))
        )

    def switch_to_new_window(self):
        current_window = self.browser.current_window_handle
        all_windows = self.browser.window_handles

        for window in all_windows:
            if window != current_window:
                self.browser.switch_to.window(window)
                return
        raise Exception("No new window found to switch to")


    def wait_until_ready_for_click(self, by, locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((by, locator))
        )
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )

    def wait_for_dom_ready(self, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def switch_to_iframe(self, index=0):
        self.browser.switch_to.default_content()
        iframes = self.browser.find_elements(By.TAG_NAME, "iframe")
        if len(iframes) <= index:
            raise IndexError(f"No iframe at index {index}")
        self.browser.switch_to.frame(iframes[index])


from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RyanairPage(BasePage):
    cookie_accept_locator = '//button[@data-ref="cookie.accept-all"]'
    login_link_locator = '//ry-log-in-button[@data-ref="main-links__log-in"]'
    email_locator = '//input[@type="email"]'
    password_locator = '//input[@type="password"]'
    sign_in_locator = '//button[@class="auth-submit__button ry-button--gradient-yellow"]'
    logout_button = '//ry-myryanair-portal-button[@data-ref="main-links__myryanair-portal"]'
    departure_locator = '//input[@id="input-button__departure"]'
    romania_locator = "//span[text()=' Румунія ']"
    bucharest_locator = '//span[text()=" Бухарест "]'
    destination_locator = '//input[@id="input-button__destination"]'
    ireland_locator = '//span[text()=" Ірландія "]'
    dublin_locator = '//span[text()=" Дублін "]'
    departure_date = '//div[@data-id="2025-04-26"]'
    return_date = '//div[@data-id="2025-05-03"]'
    search_button_locator = '//button[@aria-label="Пошук"]'
    buc_dub_conf = "//h3[contains(normalize-space(string(.)), 'Дублін до Бухарест')]"
    error_msg_invalid_pass = '//span[text()="Недійсний пароль. Залишилося спроб: 4"]'
    language_locator = '//button[@aria-label="Відкрийте вибір країни"]'
    us_locator = '//a[@href="/us/en"]'
    login_in_english_locator = '//button[normalize-space(text())="Log in"]'
    apple_store = '//a[@href="https://apps.apple.com/ua/app/ryanair/id504270602"]'
    flights_info_locator = '//a[@aria-label="Iнформацiя про рейси"]'
    past_date = By.CSS_SELECTOR, ".calendar-body__cell--disabled"
    travel_month = (By.XPATH, '//div[@data-id="лют."]')
    dep_date = (By.XPATH, '//div[@data-id="2026-02-19"]')
    ret_date = (By.XPATH, '//div[@data-id="2026-02-21"]')
    locator_price = (By.XPATH, '//flights-price-simple')
    plus_tariff_locator = (By.XPATH, '//th[@data-e2e="fare-card-plus"]')
    text_tariff1_locator = (By.XPATH, '//h3[text()=" Ви обрали тариф "]')
    text_tariff2_locator = (By.XPATH, '//h4[text()=" Plus "]')
    additional_window = (By.XPATH, '//span[text()="Увійдіть пізніше"]')
    title_locator = (By.XPATH, '//button[contains(@class, "dropdown__toggle")]')
    title_value = (By.XPATH, '//div[text()=" Пан "]')
    name_locator = (By.XPATH, '//input[@id="form.passengers.ADT-0.name"]')
    name_value = 'Test'
    surname_locator = (By.XPATH, '//input[@id="form.passengers.ADT-0.surname"]')
    surname_value = 'User'
    continue_button = (By.XPATH, '//button[text()=" Продовжити "]')

    def __init__(self, browser):
        super().__init__(browser)

    def accept_cookie(self):
        try:
            WebDriverWait(self.browser, 3).until(
                EC.visibility_of_element_located((By.XPATH, self.cookie_accept_locator))
            ).click()
        except TimeoutException:
            pass

    def click_login_link(self):
        self.find_by_xpath(self.login_link_locator).click()

    def wait_for_iframe(self):
        return self.wait_for_element(By.XPATH, '//iframe[@data-ref="kyc-iframe"]')

    def fill_in_email(self, email):
        self.find_by_xpath(self.email_locator).send_keys(email)

    def fill_in_password(self, password):
        self.find_by_xpath(self.password_locator).send_keys(password + Keys.TAB)


    def click_sign_in_button(self):
        element = self.find_by_xpath(self.sign_in_locator)
        element.click()

    def check_logout_button_presence(self):
        return self.find_by_xpath(self.logout_button).is_displayed()

    def set_departure(self):
        dep = self.find_by_xpath(self.departure_locator)
        dep.click()
        dep.clear()
        romania = self.wait_for_element(By.XPATH, self.romania_locator)
        romania.click()
        bucharest = self.wait_for_element(By.XPATH, self.bucharest_locator)
        bucharest.click()

    def destination_the_same_as_departure(self):
        try:
            element = self.wait_for_element(By.XPATH, self.bucharest_locator, timeout=3)
            return element is None
        except TimeoutException:
            return True

    def set_destination(self):
        ireland = self.wait_for_element(By.XPATH, self.ireland_locator)
        ireland.click()
        dublin = self.wait_for_element(By.XPATH, self.dublin_locator)
        dublin.click()

    def set_departure_date(self):
        dep_date = self.wait_for_element(By.XPATH, self.departure_date)
        dep_date.click()

    def set_return_date(self):
        ret_date = self.wait_for_element(By.XPATH, self.return_date)
        ret_date.click()

    def search_button_click(self):
        button = self.find_by_xpath(self.search_button_locator)
        button.click()

    def wait_for_displaying(self):
        element = self.wait_for_element(By.XPATH, self.buc_dub_conf)
        return element

    def check_alert_msg(self):
        element = self.wait_for_element(By.XPATH, self.error_msg_invalid_pass)
        return element

    def language_click(self):
        element = self.wait_for_element(By.XPATH, self.language_locator)
        element.click()

    def set_us_language(self):
        element = self.wait_for_element(By.XPATH, self.us_locator)
        element.click()

    def check_language_is_english(self):
        element = self.wait_for_element(By.XPATH, self.login_in_english_locator)
        return element

    def apple_store_transition(self):
        element = self.wait_for_element(By.XPATH, self.apple_store)
        element.click()

    def flights_info_click(self):
        element = self.wait_for_element(By.XPATH, self.flights_info_locator)
        element.click()

    def past_date_click_check(self):
        past_dates = self.browser.find_elements(*self.past_date)
        for date in past_dates:
            class_attr = date.get_attribute("class")
            if "calendar-body__cell--disabled" not in class_attr:
                raise AssertionError("Element does not have the 'disabled' class")

            try:
                date.click()
                raise AssertionError("One of the past dates was clickable")
            except Exception as e:
                if "not clickable" not in str(e) and "Other element would receive the click" not in str(e):
                    raise AssertionError(f"Unexpected exception occurred when clicking on a past date: {e}")
                continue
        return True

    def month_select(self):
        month_elements = self.wait_for_elements(*self.travel_month)
        if month_elements:
            self.browser.execute_script("arguments[0].click();", month_elements[0])
        else:
            raise Exception("Element with data-id='Feb' was not found")

    def set_dep_date(self):
        dep_date = self.wait_for_element_is_clickable(*self.dep_date)
        dep_date.click()

    def set_ret_date(self):
        ret_date = self.wait_for_element_is_clickable(*self.ret_date)
        ret_date.click()

    def set_price_for_departure(self):
        dep_price = self.wait_for_elements(*self.locator_price)[0]
        dep_price.click()

    def set_price_for_return(self):
        ret_price = self.wait_for_element_is_clickable(*self.locator_price)
        ret_price.click()

    def plus_tariff_select(self):
        plus_tariff = self.wait_for_element_is_clickable(*self.plus_tariff_locator)
        plus_tariff.click()

    def check_that_tariff_was_selected(self):
        text1 = self.wait_for_element(*self.text_tariff1_locator)
        text2 = self.wait_for_element(*self.text_tariff2_locator)
        return text1.is_displayed() and text2.is_displayed()

    def title_selection(self):
        title = self.wait_for_element_is_clickable(*self.title_locator)
        title.click()
        title_value = self.wait_for_element_is_clickable(*self.title_value)
        title_value.click()

    def name_selection(self):
        name_field = self.wait_for_element_is_clickable(*self.name_locator)
        name_field.click()
        name_field.send_keys(self.name_value)

    def surname_selection(self):
        surname_field = self.wait_for_element_is_clickable(*self.surname_locator)
        surname_field.click()
        surname_field.send_keys(self.surname_value)

    def continue_button_click(self):
        button = self.wait_for_element_is_clickable(*self.continue_button)
        button.click()

    def additional_window_skip(self, timeout=3):
        try:
            element = self.wait_for_element_is_clickable(*self.additional_window, timeout)
            element.click()
        except TimeoutException:
            pass

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class RegisterPageLocators:
    EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_SUBMIT = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    ADD_BASKET = (By.XPATH, "//form[@id='add_to_basket_form']")
    SELECTED_BOOK = (By.CSS_SELECTOR, "h1")
    ADDED_BOOK = (By.CSS_SELECTOR, "div.alertinner strong")
    BASKET_ADDED_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BOOK_PRICE = (By.XPATH, "//p[@class='price_color']")
    NOT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET = (By.CSS_SELECTOR, "span a")
    BASKET_TEXT_INFO_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    EMPTY_BASKET = (By.CSS_SELECTOR, '.row h2')

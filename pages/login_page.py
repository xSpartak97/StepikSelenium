from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators
import time


class LoginPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form isn`t presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form isn`t presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*RegisterPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.PASSWORD).send_keys('Test12345')
        self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD).send_keys('Test12345')
        self.browser.find_element(*RegisterPageLocators.REG_SUBMIT).click()

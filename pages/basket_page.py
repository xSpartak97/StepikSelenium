from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_presented(self):
        is_basket = self.browser.find_element(*BasketPageLocators.BASKET)
        is_basket.click()

    def should_text_is_basket_empty(self):
        empty_text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT_INFO_EMPTY)

        assert empty_text.text == 'Your basket is empty. Continue shopping', 'Text about empty basket isn`t appeared'

    def should_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"


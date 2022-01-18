from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_book_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        add_basket.click()

    def should_be_selected_book(self):
        a = self.browser.find_element(*ProductPageLocators.SELECTED_BOOK)
        b = self.browser.find_element(*ProductPageLocators.ADDED_BOOK)

        assert a.text == b.text, "Books are not matched"

    def should_be_added_price(self):
        a = self.browser.find_element(*ProductPageLocators.BASKET_ADDED_PRICE)
        b = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)

        assert a.text == b.text, "Price is matched"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOT_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.NOT_SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

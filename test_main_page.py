import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = BasketPage(browser, link)
        page.open()
        page.is_basket_presented()
        page.should_basket_empty()
        page.should_text_is_basket_empty()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = BasketPage(browser, link)
        page.open()
        page.is_basket_presented()
        page.should_basket_empty()
        page.should_text_is_basket_empty()


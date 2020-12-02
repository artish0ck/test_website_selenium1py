from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0","http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip()
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_product_page(), "product page is not present"
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_product_name()
    product_page.product_price_same_in_basket()
    # time.sleep(2)

@pytest.mark.skip()     #xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_product_page(), "product page is not present"
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()
    # time.sleep(10)

@pytest.mark.skip()
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_product_page(), "product page is not present"
    product_page.should_not_be_success_message()
    # time.sleep(10)

@pytest.mark.skip() #xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_product_page(), "product page is not present"
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_dissapear_success_message()
    # time.sleep(10)

@pytest.mark.skip()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    # time.sleep(5)

@pytest.mark.skip()
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)

@pytest.mark.skip()
@pytest.mark.parametrize('message', ["Your basket is empty"])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, message):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_not_basket_full()
    basket_page.is_basket_empty_message(message)

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "Afa"
        self.login_page.register_new_user(email, password)
        # time.sleep(10)
        self.login_page.should_be_authorized_user()
            
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_product_page(), "product page is not present"
        product_page.should_not_be_success_message()
        # time.sleep(10)
   
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        product_page = ProductPage(browser, link)
        product_page.open()
        assert product_page.is_product_page(), "product page is not present"
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_correct_product_name()
        product_page.product_price_same_in_basket()
        # time.sleep(2)
  




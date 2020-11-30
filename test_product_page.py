from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_product_page(), "product page is not present"
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_correct_product_name()
    product_page.product_price_same_in_basket()
     

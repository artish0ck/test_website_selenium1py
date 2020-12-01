from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def is_product_page(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION)
    
    def add_to_cart(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_correct_product_name(self):
        added_to_basket_text = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_TEXT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == added_to_basket_text.text, "wrong product added to basket"

    def product_price_same_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert product_price.text == basket_price.text, "price in basket and of product is ot the same"
        
    

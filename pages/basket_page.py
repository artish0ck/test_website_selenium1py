from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_not_basket_full(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
          "Basket is full, but it should not" 

    def is_basket_empty_message(self, message):
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert message in basket_empty_message.text, "no message 'basket is empty'"


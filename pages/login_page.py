from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "this url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER FORM is not present"

    def register_new_user(self, email, password):
        register_form_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        register_form_email.send_keys(email)
        register_form_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT)
        register_form_password.send_keys(password)
        register_form_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT_CONFIRM)
        register_form_password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        time.sleep(3)
        register_button.click()
        
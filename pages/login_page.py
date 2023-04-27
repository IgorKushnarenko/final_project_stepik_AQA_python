from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert self.browser.current_url == LOGIN_URL, 'Invalid URL for login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FIELD_FOR_LOGIN) \
               and self.is_element_present(*LoginPageLocators.FIELD_FOR_PASSWORD) \
               and self.is_element_present(*LoginPageLocators.BUTTON_FOR_LOGIN), "No element of login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FIELD_FOR_EMAIL) \
               and self.is_element_present(*LoginPageLocators.FIELD_FOR_PASSWORD_REGISTRATION) \
               and self.is_element_present(*LoginPageLocators.FIELD_FOR_PASSWORD_CONFIRMATION) \
               and self.is_element_present(*LoginPageLocators.BUTTON_FOR_REGISTRATION), "No element of registration form"

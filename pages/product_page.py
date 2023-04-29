from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_for_adding_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_FOR_ADDING_PRODUCT_TO_BASKET), \
            "No button for adding product to basket on product page"


    def add_product_to_basket(self):
        button_for_adding_product_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_FOR_ADDING_PRODUCT_TO_BASKET)
        button_for_adding_product_to_basket.click()


    def should_be_text_of_succesfull_operation(self):
        assert self.is_element_present(*ProductPageLocators.TEXT_ABOUT_SUCCESFULL_ADDING_TO_BASKET), \
            "No text about succesfull adding product to basket"

    def text_should_match_template(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        expected_text = f"{name_of_book} has been added to your basket."
        actual_text = self.browser.find_element(*ProductPageLocators.TEXT_ABOUT_SUCCESFULL_ADDING_TO_BASKET).text
        assert actual_text == expected_text, 'Text about succesfull adiing to basket doesn"t match the template'

    def prices_should_match_each_other(self):
        expected_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        actual_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert actual_price == expected_price, 'Price in message doesn"t match price of product'
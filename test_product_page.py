from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_button_for_adding_product_to_basket()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_text_of_succesfull_operation()
    product_page.text_should_match_template()
    product_page.prices_should_match_each_other()
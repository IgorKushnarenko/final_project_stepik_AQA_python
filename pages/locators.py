from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FIELD_FOR_LOGIN = (By.ID, 'id_login-username')
    FIELD_FOR_PASSWORD = (By.ID, 'id_login-password')
    BUTTON_FOR_LOGIN = (By.NAME, 'login_submit')
    FIELD_FOR_EMAIL = (By.ID, 'id_registration-email')
    FIELD_FOR_PASSWORD_REGISTRATION = (By.ID, 'id_registration-password1')
    FIELD_FOR_PASSWORD_CONFIRMATION = (By.ID, 'id_registration-password2')
    BUTTON_FOR_REGISTRATION = (By.NAME, 'registration_submit')


class ProductPageLocators():
    BUTTON_FOR_ADDING_PRODUCT_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    TEXT_ABOUT_SUCCESFULL_ADDING_TO_BASKET = (By.CLASS_NAME, 'alertinner')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner  > p > strong')
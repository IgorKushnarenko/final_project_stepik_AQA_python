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
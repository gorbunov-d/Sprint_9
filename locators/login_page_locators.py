from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORM = (By.CSS_SELECTOR, "form")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.XPATH, '//button[normalize-space()="Войти"]')

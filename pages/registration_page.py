import allure

from locators.registration_page_locators import RegistrationPageLocators as L
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    @allure.step("Заполнить регистрацию и создать аккаунт")
    def register(self, user):
        self.fill(L.FIRST_NAME, user.first_name)
        self.fill(L.LAST_NAME, user.last_name)
        self.fill(L.USERNAME, user.username)
        self.fill(L.EMAIL, user.email)
        self.fill(L.PASSWORD, user.password)
        self.click(L.SUBMIT)

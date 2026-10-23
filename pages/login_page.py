import allure

from locators.login_page_locators import LoginPageLocators as L
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Заполнить авторизацию и нажать «Войти»")
    def login(self, user):
        self.fill(L.EMAIL, user.email)
        self.fill(L.PASSWORD, user.password)
        self.click(L.SUBMIT)

    @allure.step("Проверить форму авторизации")
    def form_is_visible(self):
        return all([self.visible(L.FORM), self.visible(L.EMAIL), self.visible(L.PASSWORD), self.visible(L.SUBMIT)])

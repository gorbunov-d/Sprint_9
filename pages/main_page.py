import allure

from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Нажать «Создать аккаунт»")
    def open_registration(self):
        self.click(L.SIGN_UP)

    @allure.step("Нажать «Войти»")
    def open_login(self):
        self.click(L.SIGN_IN)

    @allure.step("Перейти на вкладку «Создать рецепт»")
    def open_recipe_creation(self):
        self.click(L.CREATE_RECIPE)

    @allure.step("Проверить кнопку «Выход»")
    def logout_is_visible(self):
        return self.visible(L.LOGOUT)

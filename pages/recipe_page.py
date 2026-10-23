import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.recipe_page_locators import RecipePageLocators as L
from pages.base_page import BasePage


class RecipePage(BasePage):
    @allure.step("Проверить карточку созданного рецепта")
    def card_is_visible(self):
        self._wait.until(EC.url_matches(r"/recipes/\d+/?$"))
        return self.visible(L.CARD)

    @allure.step("Получить название рецепта")
    def recipe_name(self):
        return self._wait.until(EC.visibility_of_element_located(L.NAME)).text

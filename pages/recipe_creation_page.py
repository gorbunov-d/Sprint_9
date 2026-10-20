import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.recipe_creation_page_locators import RecipeCreationPageLocators as L
from pages.base_page import BasePage


class RecipeCreationPage(BasePage):
    @allure.step("Заполнить все поля и создать рецепт")
    def create(self, recipe):
        self.fill(L.NAME, recipe.name)
        self.click(L.TAG)
        self.fill(L.INGREDIENT, recipe.ingredient)
        self.click(L.INGREDIENT_OPTION)
        self.fill(L.AMOUNT, recipe.amount)
        self.click(L.ADD_INGREDIENT)
        self.visible(L.ADDED_INGREDIENT)
        self.fill(L.TIME, recipe.cooking_time)
        self.fill(L.DESCRIPTION, recipe.description)
        self._wait.until(EC.presence_of_element_located(L.IMAGE)).send_keys(str(recipe.image.resolve(strict=True)))
        self.visible(L.IMAGE_PREVIEW)
        self.click(L.SUBMIT)

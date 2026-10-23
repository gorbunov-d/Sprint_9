import allure


@allure.feature("Создание рецепта")
class TestRecipeCreation:
    @allure.title("Созданный рецепт отображается в карточке с заданным названием")
    def test_created_recipe_card(self, authenticated_user, main_page, recipe_creation_page, recipe_page, recipe_data):
        main_page.open_recipe_creation()
        recipe_creation_page.create(recipe_data)
        assert recipe_page.card_is_visible(), "Карточка рецепта не отображается"
        assert recipe_page.recipe_name() == recipe_data.name, "Название рецепта отличается от заданного"

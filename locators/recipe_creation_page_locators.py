from selenium.webdriver.common.by import By


class RecipeCreationPageLocators:
    NAME = (By.XPATH, '//label[div[normalize-space()="Название рецепта"]]/input')
    TAG = (By.CSS_SELECTOR, '[class*="checkboxGroupTags"] button')
    INGREDIENT = (By.CSS_SELECTOR, 'input[class*="ingredientsInput__"]')
    INGREDIENT_OPTION = (By.XPATH, '//div[normalize-space()="абрикосы" and not(*)]')
    AMOUNT = (By.CSS_SELECTOR, 'input[class*="ingredientsAmountValue"]')
    ADD_INGREDIENT = (By.XPATH, '//div[normalize-space()="Добавить ингредиент"]')
    ADDED_INGREDIENT = (By.CSS_SELECTOR, '[class*="ingredientsAddedItemTitle"]')
    TIME = (By.XPATH, '//label[div[normalize-space()="Время приготовления"]]/input')
    DESCRIPTION = (By.TAG_NAME, "textarea")
    IMAGE = (By.CSS_SELECTOR, 'input[type="file"]')
    IMAGE_PREVIEW = (By.CSS_SELECTOR, '[class*="image"][style*="background-image"]')
    SUBMIT = (By.XPATH, '//button[normalize-space()="Создать рецепт"]')

from selenium.webdriver.common.by import By


class RecipePageLocators:
    CARD = (By.CSS_SELECTOR, '[class*="single-card__info"]')
    NAME = (By.CSS_SELECTOR, '[class*="single-card__title"]')

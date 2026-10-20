from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGN_UP = (By.CSS_SELECTOR, 'a[href="/signup"]')
    SIGN_IN = (By.CSS_SELECTOR, 'a[href="/signin"]')
    CREATE_RECIPE = (By.CSS_SELECTOR, 'a[href="/recipes/create"]')
    LOGOUT = (By.XPATH, '//*[self::button or self::a][normalize-space()="Выход"]')

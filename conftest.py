import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector

from config import BROWSER_VERSION, SELENOID_URL
from data import Recipe, User
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.recipe_creation_page import RecipeCreationPage
from pages.recipe_page import RecipePage
from pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if SELENOID_URL:
        if BROWSER_VERSION:
            options.set_capability("browserVersion", BROWSER_VERSION)
        options.set_capability("selenoid:options", {"enableVNC": False})
        browser = webdriver.Remote(command_executor=SELENOID_URL, options=options)
        browser.file_detector = LocalFileDetector()
    else:
        browser = webdriver.Chrome(options=options)
    browser.set_page_load_timeout(60)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver).open()


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def recipe_creation_page(driver):
    return RecipeCreationPage(driver)


@pytest.fixture
def recipe_page(driver):
    return RecipePage(driver)


@pytest.fixture
def new_user():
    return User.unique()


@pytest.fixture
def registered_user(main_page, registration_page, login_page, new_user):
    with allure.step("Предусловие: зарегистрировать отдельного пользователя"):
        main_page.open_registration()
        registration_page.register(new_user)
        login_page.is_at("/signin")
    return new_user


@pytest.fixture
def authenticated_user(registered_user, login_page, main_page):
    with allure.step("Предусловие: авторизовать пользователя"):
        login_page.login(registered_user)
        main_page.is_at("/recipes")
    return registered_user


@pytest.fixture
def recipe_data():
    return Recipe.unique()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    browser = item.funcargs.get("driver")
    if report.failed and browser is not None:
        from selenium.common.exceptions import WebDriverException
        try:
            allure.attach(browser.get_screenshot_as_png(), name="Ошибка в браузере", attachment_type=allure.attachment_type.PNG)
            allure.attach(browser.page_source, name="HTML страницы", attachment_type=allure.attachment_type.HTML)
        except WebDriverException:
            pass

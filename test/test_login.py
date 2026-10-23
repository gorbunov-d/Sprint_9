import allure


@allure.feature("Авторизация")
class TestLogin:
    @allure.title("После входа открывается главная страница с кнопкой «Выход»")
    def test_login_opens_recipes(self, registered_user, main_page, login_page):
        main_page.open_login()
        login_page.login(registered_user)
        assert main_page.is_at("/recipes"), "Не открыта главная страница"
        assert main_page.logout_is_visible(), "Кнопка «Выход» не отображается"

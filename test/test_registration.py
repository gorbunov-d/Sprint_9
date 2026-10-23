import allure


@allure.feature("Создание аккаунта")
class TestRegistration:
    @allure.title("После регистрации открывается страница с формой авторизации")
    def test_registration_opens_login(self, main_page, registration_page, login_page, new_user):
        main_page.open_registration()
        registration_page.register(new_user)
        assert login_page.is_at("/signin"), "Не открыта страница авторизации"
        assert login_page.form_is_visible(), "Форма авторизации не отображается"

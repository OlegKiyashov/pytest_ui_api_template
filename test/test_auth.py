import allure
from pytest_ui_api_template.page.AuthPage import AuthPage

from pytest_ui_api_template.page.MainPage import MainPage


def test_auth(browser):	
    email = "olegkiyashov@gmail.com" 
    password = "S7ks@RQsT=mQ8ZT"
    username = "Oleg K"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, password)

    main_page = MainPage(browser)
    main_page.open_menu()
    info = main_page.get_account_info()

    current_url = main_page.get_current_url()

    with allure.step("Проверить, что URL " + current_url + "заканчивается на /boards"):
        assert current_url.endswith("/boards")

    with allure.step("Проверить, что указаны данные пользователя"):
        with allure.step("Имя пользователя должно быть " + username):
            assert info[0] == username
        with allure.step("Почта пользователя должна быть " + email):
            assert info[1] == email 

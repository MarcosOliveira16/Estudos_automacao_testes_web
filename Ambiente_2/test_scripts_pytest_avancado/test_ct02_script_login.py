import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login(self):
        # instanciando os objetos a serem usados nos testes
        login_page = LoginPage()
        home_page = HomePage()

        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Verificar o login
        home_page.verificar_login_com_sucesso()

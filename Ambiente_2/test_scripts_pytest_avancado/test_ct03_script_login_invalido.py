import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
# @pytest.mark.skip
class TestCT03:
    def test_ct03_invalido_login(self):
        mensagem_error_esperado = "Epic sadface: Username and password do not match any user in this service"

        # instanciando os objetos a serem usados nos testes
        login_page = LoginPage()

        # Faz login
        login_page.fazer_login("standard_user", "senha_incorreta")

        # Verificando se o login não foi realizado
        login_page.verifica_messagem_error_login_existe()

        # verifica o texto da mensagem de error
        login_page.verificar_texto_mensagem_error_login(
            mensagem_error_esperado)

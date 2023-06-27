import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


# importando a 'fixture' definida no 'conftest'
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_add_itens(self):
        # objetos usados
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # variáveis
        produto_1 = 'Sauce Labs Backpack'
        produto_2 = 'Sauce Labs Bike Light'
        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Verificando se o elemento esta na tela - Verificar se o login foi bem sucedido
        home_page.verificar_login_com_sucesso()
        # Add itens ao carrinho
        home_page.add_ao_carrinho(produto_1)

        # Indo pro carrinho
        home_page.acessar_carrinho()

        # Vereficando o item no carrinho
        carrinho_page.verificar_produto_carrinho_existe('Sauce Labs Backpack')

        # Clicando para voltar para a tela de produtos
        carrinho_page.clicar_continuar_comprando()

        # Add itens ao carrinho
        home_page.add_ao_carrinho(produto_2)

        # Indo pro carrinho
        home_page.acessar_carrinho()

        # Vereficando os itens no carrinho
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

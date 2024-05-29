# Estudos_automacao_testes_web
Códigos iniciais sobre a temática de automação web usando as bibliotecas 'selenium' e 'pytest'. Todas as atividades foram feitas usando de sites destinados a testes sobre o referido assunto, a exemplo do 'https://www.saucedemo.com/'.


faça o mesmo para este q esta ramificado em partes. Primeira parte: import pytest
from selenium import webdriver

# variavel global
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # dar o run no test
    yield

    # teardown
    driver.quit(). segunda parte: import pytest
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
        carrinho_page.verificar_produto_carrinho_existe(produto_2). terceira parte: import pytest
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
        home_page.verificar_login_com_sucesso(). quarta parte: import pytest
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
            mensagem_error_esperado). quinta parte: import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    # abstraindo o 'find_element'
    def encontrar_elemento(self, locator):
        # retorna o locator desempacotado, ou seja, o seu conteúdo
        return self.driver.find_element(*locator)

     # abstraindo o 'find_elements'
    def encontrar_elementos(self, locator):
        # retorna o locator desempacotado, ou seja, o seu conteúdo
        return self.driver.find_elements(*locator)

    def escrever(self, locator, texto):
        self.encontrar_elemento(locator).send_keys(texto)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_existencia_elemento(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(
        ), f"O elemento \'{locator}\' não foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text

    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(
            locator), f"O elemento \'{locator}\' não existe, mas é esperado que ele exista."

    def verificar_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elementos(
            locator)) == 0, f"O elemento \'{locator}\' existe, mas é esparado que ele não exista."

    def clique_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()

    def clique_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()

    def pressionar_tecla(self, locator, key):
        element = self.encontrar_elemento(locator)
        if key == 'ENTER':
            element.send_keys(Keys.ENTER)
        elif key == 'SPACE':
            element.send_keys(Keys.SPACE)
        elif key == 'F1':
            element.send_keys(Keys.F1). sexta parte: import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# Herança
class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_iventario = (
            By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")

    def verificar_produto_carrinho_existe(self, nome_item):
        aux_item = (self.item_iventario[0],
                    self.item_iventario[1].format(nome_item))
        self.verificar_existencia_elemento(aux_item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando). setima parte: from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_iventario = (
            By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")  # 'text = {}' para alocar o item dinamecamente
        self.botao_add_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//a[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_existencia_elemento(self.titulo_pagina)

    def add_ao_carrinho(self, nome_item):
        # pegando pelo os indices o 'By.XPATH' e o XPATH em si, usando o '.format' para formata oq queremos
        # dentro desta string, nesse caso a variável 'nome_item'
        aux_item = (self.item_iventario[0],
                    self.item_iventario[1].format(nome_item))
        self.clicar(aux_item)
        self.clicar(self.botao_add_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho). oitava parte: import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


# Herança
class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        # Tuplas
        self.user_name_field = (By.ID, "user-name")
        self.passaword_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//h3[@data-test='error']")

    def fazer_login(self, usuario, senha):
        # Desempacotando a tupla e preenchendo com oq tá em 'user_name_field'
        """self.driver.find_element(*self.user_name_field).send_keys(usuario)
        self.driver.find_element(*self.passaword_field).send_keys(senha)
        self.driver.find_element(*self.login_button).click()"""

        # faz o mesmo que o de cima, porem mais intuitivo. obs: os comandos a cima não sumiram
        # apenas estão abstraidos em 'base__page'
        self.escrever(self.user_name_field, usuario)
        self.escrever(self.passaword_field, senha)
        self.clicar(self.login_button)

    def verifica_messagem_error_login_existe(self):
        self.verificar_existencia_elemento(self.error_message_login)

    def verificar_texto_mensagem_error_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi \'{texto_encontrado}\', mas era esperado \'{texto_esperado}\'"

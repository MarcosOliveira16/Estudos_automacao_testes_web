# Estudos_automacao_testes_web
Códigos iniciais sobre a temática de automação web usando as bibliotecas 'selenium' e 'pytest'. Todas as atividades foram feitas usando de sites destinados a testes sobre o referido assunto, a exemplo do 'https://www.saucedemo.com/'.

# Documentação dos Testes Automatizados com Selenium e Pytest

## Primeira Parte: Configuração Inicial e Fixture

### Código
```python
import pytest
from selenium import webdriver

# Variável global
driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # Setup
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Executar os testes
    yield

    # Teardown
    driver.quit()
```

### Descrição
Este trecho de código configura o ambiente de testes usando `pytest` e `selenium`. A fixture `setup_teardown` inicializa o navegador Microsoft Edge, define um tempo de espera implícito de 5 segundos, maximiza a janela do navegador e navega para a página inicial do site `https://www.saucedemo.com/`. Após a execução dos testes, o navegador é fechado.

## Segunda Parte: Teste de Adição de Itens ao Carrinho

### Código
```python
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

# Importando a 'fixture' definida no 'conftest'
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_add_itens(self):
        # Objetos usados
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        # Variáveis
        produto_1 = 'Sauce Labs Backpack'
        produto_2 = 'Sauce Labs Bike Light'
        
        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Verificando se o login foi bem-sucedido
        home_page.verificar_login_com_sucesso()
        
        # Adicionando itens ao carrinho
        home_page.add_ao_carrinho(produto_1)
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe('Sauce Labs Backpack')

        # Continuar comprando
        carrinho_page.clicar_continuar_comprando()
        home_page.add_ao_carrinho(produto_2)
        home_page.acessar_carrinho()

        # Verificando itens no carrinho
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)
```

### Descrição
Este teste realiza o login no site, verifica o sucesso do login, adiciona dois itens ao carrinho, e verifica se os itens foram adicionados corretamente. A fixture `setup_teardown` é utilizada para garantir que o navegador seja configurado e finalizado corretamente.

## Terceira Parte: Teste de Login

### Código
```python
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login(self):
        # Instanciando os objetos
        login_page = LoginPage()
        home_page = HomePage()

        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Verificar o login
        home_page.verificar_login_com_sucesso()
```

### Descrição
Este teste verifica se o login é realizado com sucesso no site `https://www.saucedemo.com/`. Utiliza as classes `LoginPage` e `HomePage` para interagir com a página de login e a página inicial.

## Quarta Parte: Teste de Login Inválido

### Código
```python
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_invalido_login(self):
        mensagem_error_esperado = "Epic sadface: Username and password do not match any user in this service"

        # Instanciando os objetos
        login_page = LoginPage()

        # Faz login
        login_page.fazer_login("standard_user", "senha_incorreta")

        # Verificando se o login não foi realizado
        login_page.verifica_messagem_error_login_existe()

        # Verifica o texto da mensagem de erro
        login_page.verificar_texto_mensagem_error_login(mensagem_error_esperado)
```

### Descrição
Este teste verifica se o login inválido exibe a mensagem de erro correta. Um login com senha incorreta é tentado e a presença e o conteúdo da mensagem de erro são validados.

## Quinta Parte: Classe BasePage

### Código
```python
import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    # Abstraindo o 'find_element'
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    # Abstraindo o 'find_elements'
    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, texto):
        self.encontrar_elemento(locator).send_keys(texto)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_existencia_elemento(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text

    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), f"O elemento '{locator}' não existe, mas é esperado que ele exista."

    def verificar_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, f"O elemento '{locator}' existe, mas é esperado que ele não exista."

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
            element.send_keys(Keys.F1)
```

### Descrição
A classe `BasePage` fornece métodos básicos para interação com elementos na página, incluindo encontrar elementos, clicar, escrever, verificar a existência de elementos, e esperar que elementos apareçam. Essa classe é utilizada como base para outras classes de página.

## Sexta Parte: Classe CarrinhoPage

### Código
```python
import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CarrinhoPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.item_iventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")

    def verificar_produto_carrinho_existe(self, nome_item):
        aux_item = (self.item_iventario[0], self.item_iventario[1].format(nome_item))
        self.verificar_existencia_elemento(aux_item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)
```

### Descrição
A classe `CarrinhoPage` herda de `BasePage` e fornece métodos específicos para a página do carrinho, como verificar se um produto está no carrinho e clicar no botão "continuar comprando".

## Sétima Parte: Classe HomePage

### Código
```python
from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_iventario = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")
        self.botao_add_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//a[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_existencia_elemento(self.titulo_pagina)

    def add_ao_carrinho(self, nome_item):
        aux_item = (self.item_iventario[0], self.item_iventario[1].format(nome_item))
        self.clicar(aux_item)
        self.clicar(self.botao_add_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)
```

### Descrição
A classe `HomePage` herda de `BasePage` e fornece métodos específicos para a página inicial, como verificar o sucesso do login, adicionar

 itens ao carrinho e acessar o carrinho.

## Oitava Parte: Classe LoginPage

### Código
```python
import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.user_name_field = (By.ID, "user-name")
        self.passaword_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//h3[@data-test='error']")

    def fazer_login(self, usuario, senha):
        self.escrever(self.user_name_field, usuario)
        self.escrever(self.passaword_field, senha)
        self.clicar(self.login_button)

    def verifica_messagem_error_login_existe(self):
        self.verificar_existencia_elemento(self.error_message_login)

    def verificar_texto_mensagem_error_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}', mas era esperado '{texto_esperado}'"
```

### Descrição
A classe `LoginPage` herda de `BasePage` e fornece métodos específicos para a página de login, como realizar login, verificar a existência de mensagens de erro e validar o texto das mensagens de erro.

---

Esta documentação descreve a estrutura e a funcionalidade dos códigos de testes automatizados utilizando `pytest` e `selenium`, organizando-os em classes específicas para diferentes páginas e funcionalidades do site `https://www.saucedemo.com/`. Cada classe herda métodos básicos de `BasePage` para facilitar a reutilização e manutenção do código.

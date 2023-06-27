from pages.base_page import BasePage
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
        self.clicar(self.icone_carrinho)

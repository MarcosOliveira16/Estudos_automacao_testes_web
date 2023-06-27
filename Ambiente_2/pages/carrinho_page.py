import conftest
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
        self.clicar(self.botao_continuar_comprando)

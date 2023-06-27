import conftest
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

import conftest
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
            element.send_keys(Keys.F1)

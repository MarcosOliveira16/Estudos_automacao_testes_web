import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
#@pytest.mark.skip
class TestCT03:
    def test_ct03_invalido_login(self):
        driver = conftest.driver
        # Mapeando e depois preenchendo o local com um conteudo
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("senhaErrada")
        driver.find_element(By.ID, "login-button").click()

        # Verificnado se o elemento esta na tela
        # Usar 'find_elements' pois retorna falso e não indica error igual o 'find_element'
        assert len(driver.find_elements(
            By.XPATH, "//span[@class='title']")) == 0  # find_elements retorna uma lista

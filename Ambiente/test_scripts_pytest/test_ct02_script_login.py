import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_login(self):
        driver = conftest.driver
        # Mapeando e depois preenchendo o local com um conteudo
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verificnado se o elemento esta na tela
        assert driver.find_element(
            By.XPATH, "//span[@class='title']").is_displayed()

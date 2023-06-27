import pytest
from selenium.webdriver.common.by import By
import conftest


# importando a 'fixture' definida no 'conftest'
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_add_itens(self):
        driver = conftest.driver
        # Mapeando e depois preenchendo o local com um conteudo - Fazendo login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verificando se o elemento esta na tela - Verificar se o login foi bem sucedido
        assert driver.find_element(
            By.XPATH, "//span[@class='title']").is_displayed()

        # Add itens ao carrinho
        # Clicando no item para ver detalhes
        driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        # Add item ao carrinho
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        # Indo pro carrinho
        driver.find_element(
            By.XPATH, "//a[@class='shopping_cart_link']").click()
        # Verficando se o item adicionado no carrinho aparece na tela
        assert driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # Voltando para voltar para a tela de produtos
        driver.find_element(By.ID, "continue-shopping").click()
        # Clicando no item para ver detalhes
        driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        # Add item ao carrinho
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()
        # Indo pro carrinho
        driver.find_element(
            By.XPATH, "//a[@class='shopping_cart_link']").click()
        # Verficando se os itens adicionado no carrinho aparece na tela
        assert driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()

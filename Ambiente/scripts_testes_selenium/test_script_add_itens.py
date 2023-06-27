from selenium import webdriver
from selenium.webdriver.common.by import By

# Logando no site
browser = webdriver.Edge()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get("https://www.saucedemo.com/")

# Mapeando e depois preenchendo o local com um conteudo - Fazendo login
browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()

# Verificando se o elemento esta na tela - Verificar se o login foi bem sucedido
assert browser.find_element(By.XPATH, "//span[@class='title']").is_displayed()

# Add itens ao carrinho
# Clicando no item para ver detalhes
browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
# Add item ao carrinho
browser.find_element(By.XPATH, "//*[text()='Add to cart']").click()
# Indo pro carrinho
browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
# Verficando se o item adicionado no carrinho aparece na tela
assert browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# Voltando para voltar para a tela de produtos
browser.find_element(By.ID, "continue-shopping").click()
# Clicando no item para ver detalhes
browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
# Add item ao carrinho
browser.find_element(By.XPATH, "//*[text()='Add to cart']").click()
# Indo pro carrinho
browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
# Verficando se os itens adicionado no carrinho aparece na tela
assert browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()

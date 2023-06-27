import time
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
time.sleep(3)

# Verificando se o elemento esta na tela - Verificar se o login foi bem sucedido
assert browser.find_element(
    By.XPATH, "//span[@class='title']").is_displayed(), "Erro ao tentar fazer login."

# Add itens ao carrinho
# Clicando no item para ver detalhes
browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
# Add item ao carrinho
browser.find_element(By.XPATH, "//*[text()='Add to cart']").click()
# Voltando para tela incial
browser.find_element(By.ID, "back-to-products").click()
# Indo pro carrinho
browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
# Verficando se o item adicionado no carrinho aparece na tela
assert browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

# Clicando para voltar para a tela de produtos
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
time.sleep(3)

# Finalizando a compra
# Clicando em 'checkout'
browser.find_element(By.ID, "checkout").click()
# Clicando e preeenchendo o 'first name'
browser.find_element(By.ID, "first-name").send_keys("LarguraLaElekkk")
# Clicando e preeenchendo o 'last name'
browser.find_element(By.ID, "last-name").send_keys("Altura")
# Clicando e preeenchendo o 'código postal'
browser.find_element(
    By.ID, "postal-code").send_keys("Meu pix: 1a3350b6-6f6e-4196-b007-88fb3e3e9a4b")
# Indo para a pagina de revisao das infos
time.sleep(3)
browser.find_element(By.ID, "continue").click()
# Verificando se aparecem os itens selecionados
assert browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
assert browser.find_element(
    By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
# Finalizando a compra
browser.find_element(By.ID, "finish").click()
# Verificando se a compra foi bem sucedida
assert browser.find_element(
    By.XPATH, "//*[text()='Thank you for your order!']").is_displayed()
time.sleep(3)

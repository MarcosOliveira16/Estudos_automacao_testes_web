import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get("https://www.saucedemo.com/")

# Mapeando e depois preenchendo o local com um conteudo
browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("senha_invalida")
browser.find_element(By.ID, "login-button").click()

# Verificando se o login foi feito com sucesso
assert browser.find_element(
    By.XPATH, "//*[text()= 'Epic sadface: Username and password do not match any user in this service']").is_displayed(), "Erro, não aparece mensagem de erro do login"
print('Erro ao tentar fazer login.')

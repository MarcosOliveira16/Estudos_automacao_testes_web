from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get("https://www.saucedemo.com/")

# Mapeando e depois preenchendo o local com um conteudo
browser.find_element(By.ID, "user-name").send_keys("standard_user")
browser.find_element(By.ID, "password").send_keys("secret_sauce")
browser.find_element(By.ID, "login-button").click()

# Verificnado se o elemento esta na tela
assert browser.find_element(By.XPATH, "//span[@class='title']").is_displayed()

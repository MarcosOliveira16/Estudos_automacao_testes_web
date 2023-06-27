from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
#Espera até o determinado em segundos, até ser possível seguir com o teste
browser.implicitly_wait(12)

browser.maximize_window()
#Entrar em um site
browser.get("https://chercher.tech/practice/implicit-wait-example") #(self, URL)
checkbox = browser.find_element(By.XPATH, "//input[@type='checkbox']")
#Verificar se o elemento está sendo mostrado na tela
assert checkbox.is_displayed()
time.sleep(2)
print('Checkbox na tela.')
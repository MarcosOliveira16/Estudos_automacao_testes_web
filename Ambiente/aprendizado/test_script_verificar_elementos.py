from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

browser.maximize_window()
# Entrar em um site
browser.get("https://demo.applitools.com/")  # (self, URL)

user_name = browser.find_element(By.ID, "username")
checkbox_remember = browser.find_element(By.XPATH, "//*[@type='checkbox']")

# Retorna True or False, se o elemento tiver na tela (sendo mostrado)
print(user_name.is_displayed())
assert user_name.is_displayed(), 'Elemento não encontrado na tela.'


# Retorna True or False, se o campo do elemento está habilitado
print(user_name.is_enabled())
assert user_name.is_enabled(), 'Elemento não encontrado na tela.'

# Verifica se o botão de ação foi preeenchido
print(checkbox_remember.is_selected())
assert not checkbox_remember.is_selected(), 'Campo não selecionado.'
time.sleep(2)
# Aperta na caixa para preenché-la
checkbox_remember.click()
time.sleep(2)
# Verifica se o botão de ação foi preeenchido
print(checkbox_remember.is_selected())
assert checkbox_remember.is_selected(), 'Campo não selecionado.'

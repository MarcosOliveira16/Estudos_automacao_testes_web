from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

browser.maximize_window()
#Entrar em um site
browser.get("https://saucedemo.com") #(self, URL)

"""Comentado para poder demonstrar o 'find_elements'
#find_element - econtra apenas um elemento, se não encontrar, retorna error
user_name = browser.find_element(By.ID, "user-name")
passaword = browser.find_element(By.ID, "password")

#send_keys - escrever nos campos passados como paramentros os conteudos guardados com 'find_element'
user_name.send_keys("standard_user")
time.sleep(3)
passaword.send_keys("secret_sauce")
time.sleep(3)

#Boa prática
browser.quit()"""

#find_elements - encontra mais de uma elemento (se houver) e retorna uma lista,
#se não encontrar nada retorna lista vazia

auth_files = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")
#O elemento em sí
print(auth_files)
#O tamanho, como 'find_elements' cria uma lista, será a quantidade de elementos da lista
print(len(auth_files))
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

browser.maximize_window()
#Entrar em um site
browser.get("https://saucedemo.com") #(self, URL)

#find_element - econtra apenas um elemento, se não encontrar, retorna error
user_name = browser.find_element(By.ID, "user-name")
passaword = browser.find_element(By.ID, "password")
button_login = browser.find_element(By.ID, "login-button")

#send_keys - escrever nos campos passados como paramentros os conteudos guardados com 'find_element'
user_name.send_keys("standard_user")
passaword.send_keys("secret_sauce")

#Clicando no botão login
button_login.click()
time.sleep(2)

#text
products_title = browser.find_element(By.XPATH, "//*[@class='title']")
#Retorna uma string, o texto do elemento
print(products_title.text)
assert products_title.text == "Products", 'Texto imcopatível'

first_bag_img = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
#Get_attribute - pega o conteúdo do atributo selecionado
print(first_bag_img.get_attribute("alt"))
assert first_bag_img.get_attribute("alt") == 'Sauce Labs Backpack'
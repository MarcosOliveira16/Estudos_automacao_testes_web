from selenium import webdriver
import time

browser = webdriver.Edge()

#Entrar em um site
browser.get("https://saucedemo.com") #(self, URL)

#Recebe o titulo da página
print("Titulo: ", browser.title)

#Pega a URL
print("URL: ", browser.current_url)

#Retorna todo o código fonte da página fonte
print("Código fonte: ", browser.page_source)
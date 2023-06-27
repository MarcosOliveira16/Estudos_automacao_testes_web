import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

browser = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get(
    "https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

# Quando é um campo de seleção, ou seja, um 'dropdown', temos que passar o 'find_element' dentro de uma
# classe chamada 'Select'
dropdown_products = Select(browser.find_element(
    By.XPATH, "//select[@id='first']"))
dropdown_products.select_by_visible_text(
    "Google")  # selecionando por texto visivel
time.sleep(3)

dropdown_animals = Select(browser.find_element(
    By.XPATH, "//select[@id='animals']"))
dropdown_animals.select_by_value("avatar")  # selecionando por valor
time.sleep(3)
dropdown_animals.select_by_index("2")  # selecionando por indice, estilo lista
time.sleep(2)

# Seletor múltiplo
dropdown_food = Select(browser.find_element(
    By.XPATH, "//select[@id='second']"))
dropdown_food.select_by_visible_text(
    "Pizza")  # selecionando por texto visivel
time.sleep(3)
dropdown_food.select_by_visible_text(
    "Burger")  # selecionando por texto visivel
time.sleep(3)

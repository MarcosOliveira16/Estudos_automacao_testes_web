from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Edge()
browser.maximize_window()

#Entrar em um site
browser.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver") #(self, URL)

#(browser, time_out (tempo máximo que deve esperar por algo))
wait = WebDriverWait(browser, 30)


""" Comentado para os demais testes
browser.find_element(By.ID, "alert").click()
#Vou esperar 'até' (until), 'alert_is_present' - espera até o alerta está presente
wait.until(EC.alert_is_present())
time.sleep(2)

text_to_be_present_in_element
browser.find_element(By.ID, "populate-text").click()
#Vou esperar 'até' (until), 'text_to_be_present_in_element' - espera até o texto está presente no elemento
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@class='target-text']"), "Selenium Webdriver")) #(Locator, 'Texto esperado')
target_text = browser.find_element(By.XPATH, "//*[@class='target-text']").text
assert target_text == "Selenium Webdriver"
time.sleep(2)

#element_to_be_clickable
browser.find_element(By.ID, "display-other-button").click()
wait.until(EC.element_to_be_clickable((By.ID, "hidden"))) #Esperar até o elemento ser clicado
time.sleep(2)"""

checkbox = browser.find_element(By.ID, "ch")
browser.find_element(By.ID, "checkbox").click()
wait.until(EC.element_to_be_selected(checkbox))
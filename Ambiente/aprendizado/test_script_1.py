from selenium import webdriver
import time

browser = webdriver.Edge()

#Entrar em um site
browser.get("https://google.com") #(self, URL)
time.sleep(3)

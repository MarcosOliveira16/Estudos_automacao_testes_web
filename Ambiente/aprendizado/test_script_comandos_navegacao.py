from selenium import webdriver
import time

#get
#maxime_window
#refresh
#back
#forward
#close
#quit

browser = webdriver.Edge()

#Maximizar a tela
browser.maximize_window()

#Entrar em um site
browser.get("https://google.com") #(self, URL)
time.sleep(2)

#Atualiza a pagina
browser.refresh()
time.sleep(2)

browser.get("https://www.saucedemo.com")
time.sleep(2)

#Volta para pagina anterior da navegação (<-)
browser.back()
time.sleep(2)

#Vai para seguinte da navegação (->)
browser.forward()
time.sleep(2)

#Comentado para não dar error na parte do 'quit'
"""#Cria uma nova aba
browser.switch_to.new_window("tab")
time.sleep(2)

#Fecha a aba atual de navegação
browser.close()
time.sleep(2)"""

#Criando abas para demonstrar o 'quit'
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(2)

#Fecha todos os processos (navegador)
browser.quit()
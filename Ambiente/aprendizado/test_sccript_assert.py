# Assert sempre veririfca se o retorno da condição é True
"""assert True

###Assert numeros
num_esperado = 1
nunm_obtido = 2
assert num_esperado == nunm_obtido, f"Esperado {num_esperado}. Atual {nunm_obtido}"
"""
"""
###Assert text
text_esperado = 'Selenium Webdriver'
text_obtido = 'Selenium webdriver'
#Teste é case sensitive, ou seja, tem que tá exatamente igual, maiúscula e minúsculas.
##Posso usar as operações normais do python para strings.
assert text_esperado.upper() == text_obtido.upper(), f"Esperado {text_esperado}. Atual {text_obtido}"""


# assert text in string
text_esperado = 'Selenium'
text_obtido = 'Selenium Webdriver'
# Teste é case sensitive, ou seja, tem que tá exatamente igual, maiúscula e minúsculas.
# Posso usar as operações normais do python para strings.
assert text_esperado in text_obtido, f"Esperado '{text_esperado}' dentro da string Atual '{text_obtido}'"
# assert not in string
text_esperado = 'Seleniumzzz'
text_obtido = 'Selenium Webdriver'
# Teste é case sensitive, ou seja, tem que tá exatamente igual, maiúscula e minúsculas.
# Posso usar as operações normais do python para strings.
assert text_esperado not in text_obtido, f"Esperado '{text_esperado}' dentro da string Atual '{text_obtido}'"

# assert is_displayed/is_enabled/is_selected - Retornam Treu ou False

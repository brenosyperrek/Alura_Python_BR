import re

padrao = '[0-9][a-z][0-9]'
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao,texto)
print(resposta)
print (resposta.group())
#Expressões regulares

import re

texto = ("O site que estou criando é https://www.xuxuzinho.com")
url = re.findall(r"https?://www\.\w+\.\w+", texto)

print(url)
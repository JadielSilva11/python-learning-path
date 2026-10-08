#Expressões regulares

import re
texto = ("Site: http://www.jadielsilva.com.br")
url = re.findall(r"https?://[A-Za-z0-9.]+", texto)

print(url)
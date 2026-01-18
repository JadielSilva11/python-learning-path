#Expressões regulares

import re

texto = ("O CEP da minha cidade natal é 12345-000. Mas o CEP da cidade que eu moro é 54321-000\n")
cep = re.findall(r"\d{5}-\d{3}", texto)

print(cep)
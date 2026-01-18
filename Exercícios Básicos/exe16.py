#Expressões regulares

import re

textos = ("Este era o meu número antigo (88)9857-5378. Meu novo número é (88)99616-4308.\n")
telefones = re.findall(r"\(\d{2}\)\d{4,5}-\d{4}", textos)

print(telefones)
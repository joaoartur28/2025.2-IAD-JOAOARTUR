str = "X-DSPAM-Confidence:0.8475"

local = str.find(":")

numero = str[local + 1:]

valor = float(numero)
print(valor)
fhand = open('mbox-short.txt')
contador = 0
for linha in fhand:
    palavras = linha.split()
    if len(palavras) == 0 : continue
    if palavras[0] != 'De' : continue
    print(palavras[2])
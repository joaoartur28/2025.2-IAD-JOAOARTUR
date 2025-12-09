def contagem(string, letra):
    
    total = 0
    
    for caractere in string:
        if caractere == letra:
            total = total + 1 
        
    return total
            
    
resultado1 = contagem('banana', 'a')
print(resultado1)

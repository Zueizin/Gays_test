x = str(input("Digite o diretorio: "))
with open(x, 'r') as arquivo:
    tempos = [float(linha.strip()) for linha in arquivo if linha.strip()]
    
tempos.sort()
print(tempos)
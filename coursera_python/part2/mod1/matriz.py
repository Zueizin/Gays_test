def cria_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            valor = int(input(f"Digite o elemento {[i]}{[j]}: " ))
            linha.append(valor)
        matriz.append(linha)
    return matriz
def le_matriz():
    linha = int(input("Digite quantas linhas tera sua matriz: "))
    coluna = int(input("Digite quantas colunas tera sua matriz: "))
    return cria_matriz(linha,coluna)

print(le_matriz())
matriz = [[1, 2], [3, 4]]
def imprime_matriz(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if j == coluna-1:
                print(matriz[i][j], end='')
            else:    
                print(matriz[i][j], end=' ')
        print()
imprime_matriz(matriz)
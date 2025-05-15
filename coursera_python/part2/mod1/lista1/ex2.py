matriz1 = [[1,2,3],[4,5,6]]
matriz2 = [[2,3,4],[5,6,7]]

def dimensoes(matriz):
    i = len(matriz)
    j = len(matriz[0])
    return [i,j]

def soma_matrizes(matriz1,matriz2):
    if dimensoes(matriz1) == dimensoes(matriz2):
        linha = len(matriz1)
        coluna = len(matriz1[0])
        matriz3 = []
        for i in range(linha):
            nova_linha = []
            for j in range(coluna):
                valor = matriz1[i][j] + matriz2[i][j]
                nova_linha.append(valor)
            matriz3.append(nova_linha)
        return matriz3
    else:
        return False

print(soma_matrizes(matriz1,matriz2))
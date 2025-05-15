m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
m3 = [[1], [2], [3]]
m4 = [[1, 2, 3]]
def sao_multiplicaveis(matriz1,matriz2):
    linha2 = len(matriz2)
    coluna1 = len(matriz1[0])
    if coluna1 == linha2:
        return True
    else:
        return False
    
print(sao_multiplicaveis(m1,m2))
print(sao_multiplicaveis(m3,m4))
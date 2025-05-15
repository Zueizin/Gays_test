def remove_repetidos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    unicos.sort()
    return unicos
lista = [1,1,1,1,1,5,4,5,2,2,5,1,6,7,4,2,4,6,7,3,9,9,7,3,2]
print(remove_repetidos(lista))
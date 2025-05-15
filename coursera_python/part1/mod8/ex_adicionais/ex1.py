def maior_elemento(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

lista = [1,1,3,4,2,1,32,23,2,42,5,34,643,21,34,3,2,2,42,4,2]
print(maior_elemento(lista))
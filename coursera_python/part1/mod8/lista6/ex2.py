def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = i + soma
    return soma
        
lista = [1,1,1,2,3,4,4]
print(soma_elementos(lista))
def selectionSort(vet):
    for i in range(len(vet) - 1):
        menor = i
        for j in range(i, len(vet)):
            if vet[menor] > vet[j]:
                menor = j
        aux = vet[i]
        vet[i] = vet[menor]
        vet[menor] = aux
lista = [64, 25, 12, 22, 11]
selectionSort(lista)
print("Lista ordenada:", lista)
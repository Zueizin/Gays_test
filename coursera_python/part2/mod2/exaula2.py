lista = ["maca","Zuei","joao","minecraft","jogo","circles","Anime","carne"]
def lexicografica(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i].lower() < menor.lower():
            menor = lista[i]
    return menor
print(lexicografica(lista))
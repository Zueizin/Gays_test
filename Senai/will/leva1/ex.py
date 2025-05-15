# Criamos duas listas vazias
lista1 = []  # Primeira lista
lista2 = []  # Segunda lista

# Agora vamos adicionar elementos nessas listas

# Adicionamos a segunda lista (lista2) dentro da primeira lista (lista1)
lista1.append(lista2)
# Agora lista1 contém lista2 dentro dela

# Adicionamos a primeira lista (lista1) dentro da segunda lista (lista2)
lista2.append(lista1)
# Agora lista2 contém lista1 dentro dela

# Isso cria um ciclo:
# lista1 contém lista2, que contém lista1 de volta.
# Se tentarmos apagar essas listas, pode acontecer um problema,
# pois elas continuam referenciando (apontando para) uma à outra.

# Tentamos apagar as listas
del lista1
del lista2

# Tentamos imprimir as listas para ver se ainda existem
print(lista1)  # Isso vai dar erro se a lista foi realmente apagada
print(lista2)  # Isso também dará erro se a lista não existir mais

import sys  # Importamos o módulo sys

# Criamos uma lista simples
minha_lista = [1, 2, 3, 4, 5, 6, 7]

# Verificamos o tamanho da lista em bytes
tamanho = sys.getsizeof(minha_lista)

# Exibimos o tamanho
print("O tamanho da lista em memória é:", tamanho, "bytes")

# Adicionando mais elementos à lista
minha_lista.append(8)

# Verificamos o tamanho da lista em bytes novamente
tamanho = sys.getsizeof(minha_lista)

# Verificamos os elementos da lista
print("Os elementos da lista são:", minha_lista)                      # Conclusao -----> O tamanho da lista em memoria nao mudou, pelo menos com poucas,
                                                                                         # adicoes de elementos.
# Exibimos o tamanho
print("O tamanho da lista em memória é:", tamanho, "bytes")

# Deletando elementos da lista
del minha_lista[0]
del minha_lista[1]

# Verificamos o tamanho da lista em bytes novamente
tamanho = sys.getsizeof(minha_lista)

# Verificamos os elementos da lista
print("Os elementos da lista são:", minha_lista)

# Exibimos o tamanho
print("O tamanho da lista em memória é:", tamanho, "bytes")
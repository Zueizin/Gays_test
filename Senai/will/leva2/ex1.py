# Exercício 1 - ENQUEUE (Enfileirar)
# Situação real: Uma fila para comprar ingresso no cinema. Uma nova pessoa chega e entra no final da fila.
# O comando 'append' serve para adicionar um elemento no final de uma lista (fila).

fila = ["João", "Maria", "José"]  # Cria a fila inicial
print("Fila inicial:", fila)  # Mostra a fila inicial

novo_cliente = "Ana"  # Define um novo cliente que chegou
fila.append(novo_cliente)  # Adiciona Ana ao final da fila

print("Fila após chegada de Ana:", fila)  # Mostra a fila atualizada
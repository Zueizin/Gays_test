# Exercício 5 - EMPTY (Verificar se está vazia)
# Situação real: Uma secretária verifica se ainda há pacientes na sala de espera do consultório.
# O comando 'len' verifica se o número de elementos é zero (fila vazia).

fila_sala_espera = []  # Fila vazia

# O operador == serve para comparar dois valores e verificar se eles são iguais.
# Por exemplo, a expressão len(fila_sala_espera) == 0 verifica se o tamanho da fila é igual a zero.

# Já o operador = é usado para atribuir um valor a uma variável.
# Por exemplo, fila = [] significa que você está atribuindo uma lista vazia à variável fila.

if len(fila_sala_espera) == 0:  # Verifica se a fila está vazia
    print("A sala de espera está vazia.")  # Exibe mensagem de fila vazia
else:
    print("Ainda há pacientes aguardando.")  # Exibe mensagem caso ainda tenha alguém

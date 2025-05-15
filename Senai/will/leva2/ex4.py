# Exercício 4 - DEQUEUE (Desenfileirar)
# Situação real: A primeira pessoa da fila entra no consultório médico e sai da fila.
# O comando 'pop(0)' remove o primeiro elemento da lista (inicio da fila).

fila_consultorio = ["Paciente1", "Paciente2", "Paciente3"]  # Pacientes esperando
print("Fila antes do atendimento:", fila_consultorio)  # Mostra a fila antes do atendimento

paciente_atendido = fila_consultorio.pop(0)  # Remove o primeiro paciente da fila

print("Paciente atendido:", paciente_atendido)  # Exibe o paciente que saiu
print("Fila após atendimento:", fila_consultorio)  # Mostra a fila atualizada
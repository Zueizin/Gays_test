import gc  # Importamos o módulo gc, que é responsável pelo gerenciamento automático de memória no Python.

# Criamos uma lista grande para ocupar memória.
# Aqui, estamos criando uma lista que contém números de 0 até 999999.
grande_lista = [i for i in range(10000)]

# Exibimos a quantidade de objetos que podem ser coletados antes da coleta de lixo.
# O `gc.get_count()` retorna três números que representam os objetos rastreados pelo coletor de lixo.
print("Objetos coletáveis antes da coleta:", gc.get_count())

# Deletamos a lista da memória.
# Quando usamos `del grande_lista`, estamos dizendo ao Python que não precisamos mais dessa lista.
# Isso permite que o Python libere o espaço de memória que ela estava ocupando.
del grande_lista

# Chamamos o coletor de lixo manualmente para limpar a memória.
# O Python normalmente faz isso automaticamente, mas aqui estamos forçando a execução imediata.
gc.collect()

# Exibimos novamente a quantidade de objetos coletáveis após a coleta de lixo.
print("Objetos coletáveis após a coleta:", gc.get_count())



# Conclusao --> O coletor de lixo é um mecanismo que gerencia a memória do programa, liberando a memória ocupada por objetos que não são mais necessários.
# Quanto maior a quantidade de memória ocupada por objetos que não são mais necessários, maior será o tempo de execução do programa.
# Portanto, é importante liberar a memória ocupada por objetos que não são mais necessários, para garantir um melhor desempenho do programa.
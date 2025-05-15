anterior = 1
atual = 1
k = 0
n = int(input("Ate qual ira: "))
for i in range(n):
    print(anterior)
    k = anterior + atual
    anterior = atual
    atual = k

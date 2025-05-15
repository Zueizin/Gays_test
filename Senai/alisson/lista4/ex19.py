anterior = int(input("Digite qual numero dara inicio: "))
atual = int(input("Digite qual sera o segundo termo: "))
n = int(input("Ate qual ira: "))
k = 0
if n < 3:
    print("Invalido")
else:
    for i in range(n):
        print(anterior)
        k = anterior + atual
        anterior = atual
        atual = k
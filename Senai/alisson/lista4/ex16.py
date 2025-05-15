n = int(input("Digite o fatorial que deseja: "))
fatorial = 1
for i in range(n,0,-1):
    fatorial = fatorial*i
print(fatorial)
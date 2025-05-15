numeros = []
while True:
    num = int(input("Digite um número (0 para terminar): "))
    if num == 0:
        break
    numeros.append(num)
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])
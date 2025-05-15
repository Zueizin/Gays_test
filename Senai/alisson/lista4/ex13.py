inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
somatoria = 0
for i in range(inicio, fim+1,2):
    if inicio % 2 == 0:
        print(i)
    else:
        print(i+1)
    somatoria += i
print("Somatoria = ",somatoria)
n_impares = 0
n_pares = 0
for i in range(1,11):
    n = int(input("Digite um numero inteiro: "))
    if n > 0:
        if n % 2 == 0:
            n_pares += 1
        else:
            n_impares += 1
print(f"Tem {n_pares} pares e {n_impares} impares")
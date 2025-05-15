maior_numero = -999999
menor_numero = 999999
for i in range(1,11):
    num = int(input("Digite um numero: "))
    if num > maior_numero:
        maior_numero = num
    if num < menor_numero:
        menor_numero = num
print(f"O maior é {maior_numero} e o menor é {menor_numero}")
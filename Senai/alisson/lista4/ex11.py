maior_numero = 0
menor_numero = 999999999
sair = "a"
while sair != "sair":
    num = int(input("Digite um numero: "))
    if num > maior_numero:
        maior_numero = num
    if num < menor_numero:
        menor_numero = num
    sair = input("Digite sair para sair: ")
print(f"O maior numero é {maior_numero} e o menor é {menor_numero}")
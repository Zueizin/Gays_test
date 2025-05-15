n = int(input("Digite o numero que deseja decompor: "))
fator = 2
quantidade = 0
while n > 1:
    while n % fator == 0:
        quantidade = quantidade + 1
        n = n/fator
    if quantidade > 0:
        print(f"Pelo {fator} = {quantidade}")
    fator = fator + 1
    quantidade = 0
idade = int(input("Digite a idade: "))
peso = int(input("Digite o peso: "))
if idade >= 12:
    if peso >= 60:
        dosagem = 1000
    else:
        dosagem = 875
else:
    if peso >= 5 and peso <= 9:
        dosagem = 125
    elif peso > 9 and peso <= 16:
        dosagem = 250
    elif peso > 16 and peso <= 24:
        dosagem = 375
    elif peso > 24 and peso <= 30:
        dosagem = 500
    else:
        dosagem = 750
gotas = dosagem * 20

print(f"A dosagem e {dosagem}mg equivalente a {gotas} gotas")
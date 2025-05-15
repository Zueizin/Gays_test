idade = int(input("Digite a idade: "))
if idade <= 10:
    valor = 30
elif idade > 10 and idade <= 29:
    valor = 60
elif idade > 29 and idade <= 45:
    valor = 120
elif idade > 45 and idade <= 59:
    valor = 150
elif idade > 59 and idade <= 65:
    valor = 250
elif idade > 65:
    valor = 400
print(f"Valor do plano: R$ {valor:.2f}")
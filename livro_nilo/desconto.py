m = int(input('Quantos minutos voce utilizou este mes? '))
if m < 200:
	preco = 0.2
elif m < 400:
    preco = 0.18
else:
	preco = 0.15
print(f'Voce vai pagar este mes: R${m * preco:6.2f}')
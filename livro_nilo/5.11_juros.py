depositoinicial = float(input('Digite o deposito inicial: '))
mensal = float(input('Digite o valor que depositara todo mes: '))
taxa = float(input('Digite a taxa de juros: '))
meses = int(input('Digite a quantidade de meses que ficara aplicado: '))
m = 0
d = depositoinicial
while m < meses:
	c = (d + mensal) * ((taxa/100)+1)
	d = c
	m = m + 1
	print(f'O seu saldo no mes {m} e de R${c:6.3f}.')
print(f'O seu ganho total foi de R${c - depositoinicial:6.2f}')
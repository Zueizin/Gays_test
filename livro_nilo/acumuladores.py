n = 1
soma = 0
quantidade = int(input('Digite ate onde a soma ira: '))
while n <= quantidade:
	x = int(input(f'Digite o {n} numero: '))
	soma = soma + x
	n = n + 1
print(f'Soma: {soma/quantidade:6.2f}')
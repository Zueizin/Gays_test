energia = float(input('Quantos kWh voce usou neste mes? '))
instalacao = input('Qual o seu tipo de instalacao?(R, I ou C) ')
preco = 0
if instalacao == 'R' or instalacao == 'r':
	if energia <= 500:
		preco = 0.4
	else:
		preco = 0.65
if instalacao == 'I' or instalacao == 'i':
	if energia <= 5000:
		preco = 0.55
	else:
		preco = 0.6
if instalacao == 'C' or instalacao == 'c':
	if energia <= 1000:
		preco = 0.55
	else:
		preco = 0.6
else:
	print('Tipo de instalacao inesistente.')
print(f'Preco a pagar: R${energia*preco:6.2f}')
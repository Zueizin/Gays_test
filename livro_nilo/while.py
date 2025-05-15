n = int(input('Escolha a tabuada: '))
inicio = int(input('Escolha o inicio: '))
fim = int(input('Escolha ate onde vai: '))
if n == 1:
	while n <= fim:
		print(n)
		n = n + 1
elif n == 2:
	while n <= fim:
		print(n)
		n = n + 2
else:
	print('n possui essa tabuada')
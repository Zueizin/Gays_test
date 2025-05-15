n1 = float(input('Digite o primeiro digito: '))
o = input('Digite qual a operacao deseja fazer: ')
n2 = float(input('Digite o segundo digito: '))
if o == '+':
	resultado = n1 + n2
if o == '-':
	resultado = n1 - n2
if o == '*':
	resultado = n1 * n2
elif o == '/':
	if n2 == 0:
		print('error')
	else:
		resultado = n1 / n2
else:
	print('operacao invalida')
print(f'Resultado:{n1:6.2f} {o} {n2:6.2f}')
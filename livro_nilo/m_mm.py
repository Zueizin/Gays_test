s = float(input('Digite o salario para calculo do imposto: '))
base = s
imposto = 0
if base > 3000:
	imposto = imposto + ((base - 3000)* 0.35)
	base  = 3000
if base > 1000:
	imposto = imposto + ((base - 1000)* 0.2)
print(f'Salario: R${s:6.2f} Imposto a pagar: R${imposto:6.2f}')
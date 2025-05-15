v = float(input('Digite a velocidade: '))
m = (v - 80) * 5
if v > 80:
	print(f'Sua multa e de {m}')
if v <= 80:
	print('Voce n recebeu multa')

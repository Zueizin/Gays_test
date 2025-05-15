peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em m: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 20:
    print("Abaixo do peso")
elif imc >= 20 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
elif imc >= 40:
    print("Obesidade mórbida")
else:
    print("Dados inválidos")
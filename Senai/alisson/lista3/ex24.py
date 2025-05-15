idade = int(input("Digite a idade: "))
if idade >= 5 and idade <= 7:
    print("Você está na infantil A")
elif idade >= 8 and idade < 10:
    print("Você está na infantil B")
elif idade >= 11 and idade <= 13:
    print("Você está na juvenil A")
elif idade >= 14 and idade <= 17:
    print("Você está na juvenil B")
else:
    print("Você está na Sênior")
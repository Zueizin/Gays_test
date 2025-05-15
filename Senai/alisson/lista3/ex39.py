peso_na_terra = float(input("Digite o peso na Terra: "))
print()
print("Escolha o planeta: \n1 - Mercúrio \n2 - Vênus \n3 - Marte \n4 - Júpiter \n5 - Saturno \n6 - Urano")
planeta = int(input("Digite o número do planeta: "))
print()
if planeta == 1:
    peso_no_planeta = peso_na_terra * 0.37
    planeta_nome = "Mercúrio"
elif planeta == 2:
    peso_no_planeta = peso_na_terra * 0.88
    planeta_nome = "Vênus"
elif planeta == 3:
    peso_no_planeta = peso_na_terra * 0.38
    planeta_nome = "Marte"
elif planeta == 4:
    peso_no_planeta = peso_na_terra * 2.64
    planeta_nome = "Júpiter"
elif planeta == 5:
    peso_no_planeta = peso_na_terra * 1.15
    planeta_nome = "Saturno"
elif planeta == 6:
    peso_no_planeta = peso_na_terra * 1.17
    planeta_nome = "Urano"
else:
    print("Planeta inválido.")
print(f"O peso no planeta {planeta_nome} é: {peso_no_planeta:.2f}")
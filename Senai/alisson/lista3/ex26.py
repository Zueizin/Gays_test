n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
if media >= 7:
    print("Aprovado")
elif media < 7 and media >= 3:
    print("Recuperação")
else:
    print("Reprovado")
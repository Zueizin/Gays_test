frequencia = float(input("Digite a frequência: "))
nota = float(input("Digite a nota: "))
if frequencia < 75:
    print("Reprovado por falta")
elif nota < 3:
    print("Reprovado por nota")
elif nota >= 3 and nota < 7:
    print("Recuperação")
elif nota >= 7:
    print("Aprovado")
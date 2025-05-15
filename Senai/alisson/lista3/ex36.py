print("Regioes: \n1 - Norte\n2 - Nordeste\n3 - Centro-Oeste\n4 - Sul")
regiao = input("Digite o valor correspondente a sua região: ")
print()
print("Condicoes: \n1 - Somente ida\n2 - Ida e volta")
condicao = input("Digite o valor correspondente a sua condição: ")
print()
if condicao != "1" and condicao != "2":
    print("Condição inválida")
if regiao == "1":
    if condicao == "1":
        print("R$ 500,00")
    elif condicao == "2":
        print("R$ 900,00")
elif regiao == "2":
    if condicao == "1":
        print("R$ 350,00")
    elif condicao == "2":
        print("R$ 650,00")
elif regiao == "3":
    if condicao == "1":
        print("R$ 350,00")
    elif condicao == "2":
        print("R$ 600,00")
elif regiao == "4":
    if condicao == "1":
        print("R$ 300,00")
    elif condicao == "2":
        print("R$ 550,00")
else:
    print("Região inválida")
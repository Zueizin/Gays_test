prestacao = int(input("Digite o valor da prestação: "))
salario = int(input("Digite o valor do salário: "))
minimo = salario * 0.3
if prestacao <= minimo:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")
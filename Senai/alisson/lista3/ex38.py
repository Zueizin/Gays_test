mes = int(input("Digite um número de 1 a 12: "))
ipva = "nenhum"
placa = int(input("Digite os 4 ultimos números da placa do carro: "))
if placa % 10 == 1:
    ipva = 1
elif placa % 10 == 2:
    ipva = 2
elif placa % 10 == 3:
    ipva = 3
elif placa % 10 == 4:
    ipva = 4
elif placa % 10 == 5:
    ipva = 5
elif placa % 10 == 6:   
    ipva = 6
elif placa % 10 == 7:
    ipva = 7
elif placa % 10 == 8:
    ipva = 8
elif placa % 10 == 9:
    ipva = 9
elif placa % 10 == 0:
    ipva = 0
else:
    ipva = "nenhum"
if mes == ipva:
    if mes == 1:
        mes = "Janeiro"
    elif mes == 2:
        mes = "Fevereiro"
    elif mes == 3:  
        mes = "Março"
    elif mes == 4:  
        mes = "Abril"
    elif mes == 5:  
        mes = "Maio"
    elif mes == 6:
        mes = "Junho"
    elif mes == 7:
        mes = "Julho"
    elif mes == 8:
        mes = "Agosto"
    elif mes == 9:
        mes = "Setembro"
    elif mes == 10:
        mes = "Outubro"
    print(f"O IPVA vence no mês de {mes}.")

x = int(input("Digite um número: "))
if x >= -4 and x <= 4:
    print("Valor invalido")
else:
    print(f"O valor de y e {(5*x+3)/(x**2-16)**0.5}")
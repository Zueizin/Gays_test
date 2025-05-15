a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta =b**2 -4*a*c
if a == 0:
    print("Não correspondido.")
else:
    if delta > 0:
        print(f"As raizes da sua equação são: x1 = {(-b + delta**(1/2))/2*a} e x2 = {(-b - delta**(1/2))/2*a}")
    elif delta == 0:
        print(f"A sua raiz é x = {(-b/(2*a))}")
    else:
        print("Sua equação não possui resolução nos reais.")
n = int(input("Digite um numero: "))
for i in range(1,n+1):
    if n % i == 0:
        print(f"O numero {i} é divisor de {n}")
    else: 
        continue
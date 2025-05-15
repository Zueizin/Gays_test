while True:
    n = int(input("Digite um numero inteiro positivo: "))
    i = 2
    divisores = 1
    if n > 0:
        while i <= n and divisores <= 2:
            if n % i == 0:
                divisores += 1
            i += 1
        if divisores == 2:
            print("primo")
        else:
            print("não primo")
    else:
        break
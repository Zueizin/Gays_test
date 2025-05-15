n = 0
def fatorial(n):
    if n < 0:
        return False
    elif n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
while n != -1:
    n = int(input("Digite um número inteiro não-negativo(-1 para sair): "))
    print(fatorial(n))
    if n == -1:
        break
